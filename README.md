this is all command to run application 

1- python manage.py makemigrations account blog users company customer box coin passport employee bus expense  trip reservation ked

2- python manage.py migrate

3- python manage.py loaddata data.json

4- python manage.py runserver

/************  extra command ***************/
winpty python manage.py createsuperuser
python manage.py dumpdata myapp > databasedump.json
django-admin makemessages --all
django-admin compilemessages
