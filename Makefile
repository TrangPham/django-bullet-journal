HOST=127.0.0.1
PORT=8028

run:
	python manage.py runserver $(PORT)

migrate:
	python manage.py migrate $(APP) $(OPTIONS)

migrations:
	python manage.py migrations $(APP)

shell:
	python manage.py shell
