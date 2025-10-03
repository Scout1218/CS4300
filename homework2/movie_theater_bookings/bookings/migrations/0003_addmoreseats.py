from django.db import migrations

def add_seats(apps, schema_editor):
    Seat = apps.get_model("bookings", "Seat")
    wanted = [*(f"A{i}" for i in range(1, 11)), *(f"B{i}" for i in range(1, 11)), *(f"C{i}" for i in range(1, 11))]
    for num in wanted:
        Seat.objects.get_or_create(seat_number=num, defaults={"booking_status": "available"})

def remove_seats(apps, schema_editor):
    Seat = apps.get_model("bookings", "Seat")
    Seat.objects.filter(seat_number__regex=r"^[ABC](10|[1-9])$").delete()

class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0002_demo_data"),  
    ]
    operations = [
        migrations.RunPython(add_seats, reverse_code=remove_seats),
    ]