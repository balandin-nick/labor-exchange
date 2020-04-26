#!/usr/bin/env sh

set -e

case "$1" in
    django-server)
        exec python manage.py runserver 0.0.0.0:8000
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