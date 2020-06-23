HOST=127.0.0.1
PORT=8028

run:
	python manage.py runserver $(PORT)

migrate:
	make migrations $(APP)
	python manage.py migrate $(APP) $(OPTIONS)

migrations:
	python manage.py makemigrations $(APP)

shell:
	python manage.py shell

reset-db:
	rm db.sqlite3
	make migrate
	python manage.py createsuperuser