from django.db import migrations
from datetime import date

def create_demo_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Movie = apps.get_model("bookings", "Movie")
    Seat = apps.get_model("bookings", "Seat")
    Booking = apps.get_model("bookings", "Booking")

    # Demo user (for booking ownership)
    user, _ = User.objects.get_or_create(username="demo", defaults={"is_staff": False, "is_superuser": False})
    if not user.password:
        # set an unusable password; you can set a real one later via createsuperuser/admin
        user.set_unusable_password()
        user.save(update_fields=["password"])

    # Movies
    m1, _ = Movie.objects.get_or_create(
        title="Inception",
        defaults={
            "description": "A mind-bending thriller where dreams can be controlled.",
            "release_date": date(2010, 7, 16),
            "duration": 148,
        },
    )
    m2, _ = Movie.objects.get_or_create(
        title="Interstellar",
        defaults={
            "description": "A journey through space and time to save humanity.",
            "release_date": date(2014, 11, 7),
            "duration": 169,
        },
    )

    # Seats
    a1, _ = Seat.objects.get_or_create(seat_number="A1", defaults={"booking_status": "available"})
    a2, _ = Seat.objects.get_or_create(seat_number="A2", defaults={"booking_status": "available"})
    b1, _ = Seat.objects.get_or_create(seat_number="B1", defaults={"booking_status": "available"})

    # One booking so history shows something; mark seat booked
    if not Booking.objects.filter(seat=a1, movie=m1).exists():
        a1.booking_status = "booked"
        a1.save(update_fields=["booking_status"])
        Booking.objects.create(user=user, movie=m1, seat=a1)

def remove_demo_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Movie = apps.get_model("bookings", "Movie")
    Seat = apps.get_model("bookings", "Seat")
    Booking = apps.get_model("bookings", "Booking")

    # Clean up only what we created
    Booking.objects.filter(user__username="demo").delete()
    Seat.objects.filter(seat_number__in=["A1", "A2", "B1"]).update(booking_status="available")
    Seat.objects.filter(seat_number__in=["A1", "A2", "B1"]).delete()
    Movie.objects.filter(title__in=["Inception", "Interstellar"]).delete()
    User.objects.filter(username="demo").delete()

class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),  # safe dependency on auth
    ]

    operations = [
        migrations.RunPython(create_demo_data, reverse_code=remove_demo_data),
    ]
