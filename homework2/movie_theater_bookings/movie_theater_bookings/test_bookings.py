import pytest
from datetime import date
from django.urls import reverse
from rest_framework.test import APIClient
from bookings.models import Movie, Seat, Booking


@pytest.fixture
def movie(db):
    return Movie.objects.create(
        title="Inception",
        description="Dream thriller",
        release_date=date(2010, 7, 16),
        duration=148,
    )

@pytest.fixture
def seats(db):
    s1 = Seat.objects.create(seat_number="A1")
    s2 = Seat.objects.create(seat_number="A2")
    return [s1, s2]

# ---------- Model tests ----------
def test_seat_number_unique(db):
    Seat.objects.create(seat_number="X1")
    with pytest.raises(Exception):
        Seat.objects.create(seat_number="X1")

def test_booking_unique_per_movie_seat(db, movie, seats):
    Booking.objects.create(movie=movie, seat=seats[0])
    with pytest.raises(Exception):
        Booking.objects.create(movie=movie, seat=seats[0])

# ---------- HTML view tests ----------
@pytest.mark.django_db
def test_movie_list_view(client, movie):
    url = reverse("movie_list")
    r = client.get(url)
    assert r.status_code == 200
    body = r.content.decode()
    assert "Inception" in body

@pytest.mark.django_db
def test_book_seat_flow(client, movie, seats):
    url = reverse("book_seat", args=[movie.id])
    # GET shows seats
    r = client.get(url)
    assert r.status_code == 200
    body = r.content.decode()
    assert "A1" in body and "A2" in body

    # POST to book A1
    r = client.post(url, {"seat_id": seats[0].id}, follow=True)
    assert r.status_code == 200
    assert Booking.objects.filter(movie=movie, seat=seats[0]).exists()

@pytest.mark.django_db
def test_booking_history_view(client, movie, seats):
    Booking.objects.create(movie=movie, seat=seats[1])
    url = reverse("booking_history")
    r = client.get(url)
    assert r.status_code == 200
    assert "A2" in r.content.decode()

# ---------- API tests ----------
@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_api_list_movies(api_client, movie):
    r = api_client.get("/api/movies/")
    assert r.status_code == 200
    data = r.json()
    # DefaultRouter may return a list or a dict with 'results' if pagination added;
    # we disabled pagination in settings for stability.
    assert isinstance(data, list)
    assert any(m["title"] == "Inception" for m in data)

@pytest.mark.django_db
def test_api_book_seat(api_client, movie, seats):
    r = api_client.post(f"/api/seats/{seats[0].id}/book/", {"movie": movie.id}, format="json")
    assert r.status_code == 201
    seats[0].refresh_from_db()
    assert seats[0].booking_status == "booked"
    assert Booking.objects.filter(movie=movie, seat=seats[0]).exists()

@pytest.mark.django_db
def test_api_book_seat_conflict(api_client, movie, seats):
    api_client.post(f"/api/seats/{seats[1].id}/book/", {"movie": movie.id}, format="json")
    r2 = api_client.post(f"/api/seats/{seats[1].id}/book/", {"movie": movie.id}, format="json")
    assert r2.status_code == 409
