#!/bin/bash
set -euo --pipefail

python manage.py migrate

# wsgiref (django-admin runserver)
# python manage.py runserver 0.0.0.0:8000

# gunicorn
# poetry run gunicorn --bind 0.0.0.0:8000 --workers 1 mysite.wsgi:application

# uvicorn
poetry run uvicorn --host 0.0.0.0 --port 8000 --workers 1 mysite.asgi:application
