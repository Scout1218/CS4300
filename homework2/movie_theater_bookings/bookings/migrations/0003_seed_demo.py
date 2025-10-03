from django.db import migrations
from datetime import date

def create_demo(apps, schema_editor):
    Movie = apps.get_model("bookings", "Movie")
    Seat = apps.get_model("bookings", "Seat")
    Booking = apps.get_model("bookings", "Booking")

    # Movies (idempotent via get_or_create)
    movies_data = [
        {
            "title": "Inception",
            "description": "A mind-bending thriller where dreams can be controlled.",
            "release_date": date(2010, 7, 16),
            "duration": 148,
        },
        {
            "title": "Interstellar",
            "description": "A journey through space and time to save humanity.",
            "release_date": date(2014, 11, 7),
            "duration": 169,
        },
        {
            "title": "Tenet",
            "description": "A temporal espionage thriller.",
            "release_date": date(2020, 9, 3),
            "duration": 150,
        },
    ]
    movie_objs = []
    for m in movies_data:
        obj, _ = Movie.objects.get_or_create(title=m["title"], defaults=m)
        movie_objs.append(obj)

    # Seats A1–A20, B1–B20, C1–C20 (idempotent)
    rows = "ABC"
    count = 20
    for r in rows:
        for i in range(1, count + 1):
            Seat.objects.get_or_create(
                seat_number=f"{r}{i}",
                defaults={"booking_status": "available"},
            )

    # Make a couple of sample bookings so history isn't empty (idempotent)
    # A1 booked for Inception, B1 booked for Interstellar
    try:
        m_inception = Movie.objects.get(title="Inception")
        m_interstellar = Movie.objects.get(title="Interstellar")
        a1 = Seat.objects.get(seat_number="A1")
        b1 = Seat.objects.get(seat_number="B1")

        if not Booking.objects.filter(movie=m_inception, seat=a1).exists():
            a1.booking_status = "booked"
            a1.save(update_fields=["booking_status"])
            Booking.objects.create(movie=m_inception, seat=a1)

        if not Booking.objects.filter(movie=m_interstellar, seat=b1).exists():
            b1.booking_status = "booked"
            b1.save(update_fields=["booking_status"])
            Booking.objects.create(movie=m_interstellar, seat=b1)

    except (Movie.DoesNotExist, Seat.DoesNotExist):
        # Safe to ignore; seats/movies may not exist if prior steps failed
        pass

def remove_demo(apps, schema_editor):
    Movie = apps.get_model("bookings", "Movie")
    Seat = apps.get_model("bookings", "Seat")
    Booking = apps.get_model("bookings", "Booking")

    # Delete only the demo bookings and seats/movies we created
    Booking.objects.filter(
        movie__title__in=["Inception", "Interstellar", "Tenet"]
    ).delete()

    # Reset seat statuses for the ones we touched, then remove demo seats
    for num in ["A1", "B1"]:
        try:
            s = Seat.objects.get(seat_number=num)
            s.booking_status = "available"
            s.save(update_fields=["booking_status"])
        except Seat.DoesNotExist:
            pass

    # Remove the demo seats if they match our naming convention
    Seat.objects.filter(seat_number__regex=r"^[ABC](?:[1-9]|1\d|20)$").delete()

    # Remove demo movies
    Movie.objects.filter(title__in=["Inception", "Interstellar", "Tenet"]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0002_remove_booking_user"),  # <-- adjust if your latest migration has a different name/number
    ]

    operations = [
        migrations.RunPython(create_demo, reverse_code=remove_demo),
    ]
