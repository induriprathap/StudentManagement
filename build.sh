#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate

python manage.py shell -c "from students.models import Course; [Course.objects.get_or_create(name=name) for name in ['Python', 'Data Science', 'Machine Learning', 'Django']]"