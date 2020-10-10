#!/bin/sh

# This assumes you've created a virtual environment and installed Gunicorn
# See the docs for instructions

source app/bin/activate
echo "PORT - " >> "things.txt"
echo $PORT >> "things.txt"
echo "HOST - " >> "things.txt"
echo $HOST >> "things.txt"
# Flask
#gunicorn app:app -b $HOST:$PORT -w 1
# Django (replace <name> with the name of your application)
gunicorn praneethbhandaru.wsgi -b $HOST:$PORT -w 1
