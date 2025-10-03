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
    ...

    @action(detail=True, methods=["post"])
    def book(self, request, pk=None):
        seat = self.get_object()

        # Accept JSON, form, or ?movie=...
        movie_id = (
            request.data.get("movie")
            or request.POST.get("movie")
            or request.query_params.get("movie")
        )
        if not movie_id:
            return Response({"detail": "movie is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "movie not found"}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            seat = Seat.objects.select_for_update().get(pk=seat.pk)
            if Booking.objects.filter(movie=movie, seat=seat).exists():
                return Response({"detail": "already booked for this movie"}, status=status.HTTP_409_CONFLICT)
            if seat.booking_status != Seat.Status.AVAILABLE:
                return Response({"detail": "seat not available"}, status=status.HTTP_409_CONFLICT)

            seat.booking_status = Seat.Status.BOOKED
            seat.save(update_fields=["booking_status"])
            booking = Booking.objects.create(movie=movie, seat=seat)

        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("movie", "seat", "user").order_by("-booking_date")
    serializer_class = BookingSerializer

    def get_queryset(self):
        # If user is authenticated, show their own bookings by default
        qs = super().get_queryset()
        if self.request.user and self.request.user.is_authenticated:
            return qs.filter(user=self.request.user)
        return qs
