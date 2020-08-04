#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn --access-logfile - --workers 4 --timeout 300 --reload \
  --bind web:8443 screenshot_telegram_bot.wsgi:application
