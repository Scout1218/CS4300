from django.urls import path
from . import web_views

urlpatterns = [
    path("", web_views.movie_list, name="movie_list"),
    path("movies/<int:movie_id>/book/", web_views.book_seat, name="book_seat"),
    path("bookings/history/", web_views.booking_history, name="booking_history"),
]
