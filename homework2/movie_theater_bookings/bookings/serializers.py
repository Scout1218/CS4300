from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source="movie.title")
    seat_number = serializers.ReadOnlyField(source="seat.seat_number")

    class Meta:
        model = Booking
        fields = ["id", "movie", "movie_title", "seat", "seat_number", "user", "booking_date"]
        read_only_fields = ["booking_date"]
