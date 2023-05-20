run:
	python run.py


.PHONY:
runserver:
	pdm run python manage.py runserver 


.PHONY:
makemigrations:
	pdm run python manage.py makemigrations


.PHONY:
migrate:
	pdm run python manage.py migrate


.PHONY:
createsuperuser:
	pdm run python manage.py createsuperuser

