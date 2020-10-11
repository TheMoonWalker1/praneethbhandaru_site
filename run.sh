#!/bin/sh

source app/bin/activate

gunicorn praneethbhandaru.wsgi -b $HOST:$PORT -w 1
