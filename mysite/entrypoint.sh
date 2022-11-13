#!/bin/bash

poetry run python manage.py migrate

# wsgiref (django-admin runserver)
# poetry run python manage.py runserver 0.0.0.0:8000

# gunicorn
poetry run gunicorn --bind 0.0.0.0:8000 --workers 1 mysite.wsgi
