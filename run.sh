#!/bin/sh

source app/bin/activate

pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
echo "from django.contrib.auth.models import User; User.objects.create_superuser('themoonwalker_', 'praneethsbhandaru.com', 'admin')" | python manage.py shell

gunicorn praneethbhandaru.wsgi -b $HOST:$PORT -w 1
