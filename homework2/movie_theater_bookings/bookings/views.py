from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by("seat_number")
    serializer_class = SeatSerializer

    @action(detail=True, methods=["post"])
    def book(self, request, pk=None):
        """POST /api/seats/{id}/book/ with JSON: {"movie": <movie_id>}"""
        seat = self.get_object()
        movie_id = request.data.get("movie")
        if not movie_id:
            return Response({"detail": "movie is required"}, status=400)
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "movie not found"}, status=404)

        user = request.user if request.user.is_authenticated else None
        if not user:
            # allow passing a user id for quick testing without auth
            uid = request.data.get("user")
            if not uid:
                return Response({"detail": "user is required (auth or user id)"},
                                status=400)
            user = get_user_model().objects.get(pk=uid)

        if seat.booking_status != Seat.Status.AVAILABLE:
            return Response({"detail": "Seat not available"}, status=409)

        with transaction.atomic():
            seat = Seat.objects.select_for_update().get(pk=seat.pk)
            if seat.booking_status != Seat.Status.AVAILABLE:
                return Response({"detail": "Seat just taken"}, status=409)
            seat.booking_status = Seat.Status.BOOKED
            seat.save(update_fields=["booking_status"])
            booking = Booking.objects.create(user=user, movie=movie, seat=seat)

        return Response(BookingSerializer(booking).data, status=201)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("movie", "seat", "user").order_by("-booking_date")
    serializer_class = BookingSerializer

    def get_queryset(self):
        # If user is authenticated, show their own bookings by default
        qs = super().get_queryset()
        if self.request.user and self.request.user.is_authenticated:
            return qs.filter(user=self.request.user)
        return qs
