#!/usr/bin/env sh

set -e

case "$1" in
    runserver)
        exec python manage.py runserver 0.0.0.0:8000 --nostatic
        ;;
    gunicorn)
        exec gunicorn labor_exchange.wsgi:application --bind 0.0.0.0:8000
        ;;
    makemigrations)
        exec python manage.py makemigrations $2
        ;;
    migrate)
        exec python manage.py migrate
        ;;
    analyze)
        ./analyze.sh
        ;;
    tests)
        echo 'Tests'
        ;;
    *)
        exec "$@"
esac