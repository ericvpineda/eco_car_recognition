#!/bin/bash
if [ "$1" == "venv" ]; then
    source .venv/Scripts/activate
elif [ "$1" == "livereload" ]; then
    python manage.py livereload
elif [ "$1" == "runserver" ]; then
    python manage.py runserver
elif [ "$1" == "freeze" ]; then
    pip freeze > requirements.txt
fi