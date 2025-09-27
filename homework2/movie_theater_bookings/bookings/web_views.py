from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .models import Movie, Seat, Booking

def movie_list(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})

from django.db import IntegrityError, transaction

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, pk=seat_id)

        user = request.user if request.user.is_authenticated else get_user_model().objects.get_or_create(username="demo")[0]

        try:
            with transaction.atomic():
                seat = Seat.objects.select_for_update().get(pk=seat.pk)
                if Booking.objects.filter(movie=movie, seat=seat).exists():
                    raise IntegrityError("already-booked-for-movie")
                if seat.booking_status != Seat.Status.AVAILABLE:
                    raise IntegrityError("seat-not-available")

                seat.booking_status = Seat.Status.BOOKED
                seat.save(update_fields=["booking_status"])

                # use current user if logged in; otherwise a demo user
                User = get_user_model()
                user = request.user if request.user.is_authenticated else User.objects.get_or_create(username="demo")[0]

                Booking.objects.create(movie=movie, seat=seat, user=user)

            return redirect("booking_history")


        except IntegrityError:
            available = Seat.objects.filter(
                booking_status=Seat.Status.AVAILABLE
            ).exclude(
                bookings__movie=movie
            ).order_by("seat_number")

            return render(request, "bookings/seat_booking.html", {
                "movie": movie,
                "available_seats": available,
                "message": "Seat was just taken. Pick another."
            })

    # GET — populate dropdown (use the same filtered queryset)
    available = Seat.objects.filter(
        booking_status=Seat.Status.AVAILABLE
    ).exclude(
        bookings__movie=movie
    ).order_by("seat_number")

    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "available_seats": available
    })


def booking_history(request):
    bookings = (
        Booking.objects
        .select_related("movie", "seat")
        .order_by("-booking_date")
    )
    return render(request, "bookings/booking_history.html", {"bookings": bookings})


