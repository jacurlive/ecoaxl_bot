run:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

mig:
	python manage.py makemigrations
	python manage.py migrate

req:
	pip freeze > requirements.txt

venv:
	source venv/bin/activate
