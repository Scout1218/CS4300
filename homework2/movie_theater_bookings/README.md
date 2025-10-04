Movie Theater Bookings

A simple Django web app that allows users to view movies, select available seats, and make seat bookings.
Developed for CS 4300 Homework 2.


Live Demo
You can access the deployed version here:
https://cs4300-hw2.onrender.com

Running Locally
1. Clone repo: https://github.com/Scout1218/CS4300

2. activate venv: python -m venv venv, source venv/bin/activate

3. install dependenciest pip install -r requirments.txt

4. cd /homework2/movie_theater_bookings

5. apply migrations and insert demo data: python manage.py migrate

6. run dev server python manage.py runserver

structure:
movie_theater_bookings/
│
├── bookings/                   # Main Django app
│   ├── migrations/             # Includes demo data seeding
│   ├── templates/bookings/     # HTML templates
│   ├── views.py                # API and web views
│   ├── web_views.py            # User-facing pages
│   ├── urls.py                 # API endpoints
│   ├── web_urls.py             # Web routes
│   ├── tests.py                # Unit tests
│   └── serializers.py          # REST framework serializers
│
├── movie_theater_bookings/
│   ├── settings.py             # Main configuration
│   ├── urls.py                 # Root URL config
│   └── asgi.py / wsgi.py
│
├── build.sh                    # Render build script
├── requirements.txt
└── manage.py

Run tests with python manage.py test

