# bookings/tests.py
from datetime import date
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking


class ModelTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="Dream thriller",
            release_date=date(2010, 7, 16),
            duration=148,
        )
        self.a1 = Seat.objects.create(seat_number="A1")
        self.a2 = Seat.objects.create(seat_number="A2")

    def test_seat_number_unique(self):
        with self.assertRaises(Exception):
            Seat.objects.create(seat_number="A1")

    def test_booking_unique_per_movie_seat(self):
        Booking.objects.create(movie=self.movie, seat=self.a1)
        with self.assertRaises(Exception):
            Booking.objects.create(movie=self.movie, seat=self.a1)

    def test_strs_exist(self):
        self.assertIn("Inception", str(self.movie))
        self.assertIn("A1", str(self.a1))


class HtmlViewTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Interstellar",
            description="Space epic",
            release_date=date(2014, 11, 7),
            duration=169,
        )
        self.a1 = Seat.objects.create(seat_number="B1")
        self.a2 = Seat.objects.create(seat_number="B2")

    def test_movie_list_renders(self):
        url = reverse("movie_list")  # If you namespaced, use reverse("bookings:movie_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Interstellar", resp.content.decode())

    def test_book_seat_post_creates_booking_and_marks_seat_booked(self):
        url = reverse("book_seat", args=[self.movie.id])  # or ("bookings:book_seat", [id])
        # GET shows available seats
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        body = resp.content.decode()
        self.assertIn("B1", body)
        self.assertIn("B2", body)

        # POST to book B1
        resp = self.client.post(url, {"seat_id": self.a1.id}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Booking.objects.filter(movie=self.movie, seat=self.a1).exists())
        self.a1.refresh_from_db()
        self.assertEqual(self.a1.booking_status, Seat.Status.BOOKED)

    def test_booking_history_lists_rows(self):
        Booking.objects.create(movie=self.movie, seat=self.a2)
        url = reverse("booking_history")  # or "bookings:booking_history"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("B2", resp.content.decode())


class ApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # setUpTestData runs once per class (faster than setUp)
        cls.client_api = APIClient()
        cls.movie = Movie.objects.create(
            title="Tenet",
            description="Temporal thriller",
            release_date=date(2020, 9, 3),
            duration=150,
        )
        cls.s1 = Seat.objects.create(seat_number="C1")
        cls.s2 = Seat.objects.create(seat_number="C2")

    def test_list_movies(self):
        r = self.client_api.get("/api/movies/")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data = r.json()
        self.assertTrue(any(m["title"] == "Tenet" for m in data))

    '''def test_book_seat_success(self):
        r = self.client_api.post(f"/api/seats/{self.s1.id}/book/", {"movie": self.movie.id}, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.s1.refresh_from_db()
        self.assertEqual(self.s1.booking_status, Seat.Status.BOOKED)
        self.assertTrue(Booking.objects.filter(movie=self.movie, seat=self.s1).exists())

    def test_book_seat_conflict(self):
        # First booking
        self.client_api.post(f"/api/seats/{self.s2.id}/book/", {"movie": self.movie.id}, format="json")
        # Second booking for same (movie, seat) should conflict
        r2 = self.client_api.post(f"/api/seats/{self.s2.id}/book/", {"movie": self.movie.id}, format="json")
        self.assertEqual(r2.status_code, status.HTTP_409_CONFLICT)
'''