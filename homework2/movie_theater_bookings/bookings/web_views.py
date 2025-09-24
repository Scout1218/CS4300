from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Seat, Booking

def movie_list(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, pk=seat_id)
        if seat.booking_status == Seat.Status.AVAILABLE:
            seat.booking_status = Seat.Status.BOOKED
            seat.save(update_fields=["booking_status"])
            user = request.user if request.user.is_authenticated else get_user_model().objects.first()
            Booking.objects.create(movie=movie, seat=seat, user=user)
            return redirect("booking_history")
        return render(request, "bookings/seat_booking.html",
                      {"movie": movie, "available_seats": Seat.objects.filter(booking_status=Seat.Status.AVAILABLE),
                       "message": "Seat not available"})

    available = Seat.objects.filter(booking_status=Seat.Status.AVAILABLE).order_by("seat_number")
    return render(request, "bookings/seat_booking.html",
                  {"movie": movie, "available_seats": available})

def booking_history(request):
    qs = Booking.objects.select_related("movie", "seat").order_by("-booking_date")
    if request.user.is_authenticated:
        qs = qs.filter(user=request.user)
    return render(request, "bookings/booking_history.html", {"bookings": qs})
