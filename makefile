web:
	docker compose up  --build

dev:
	poetry run ./manage.py runserver

celery:
	poetry run celery -A __project__ worker --loglevel=info

enter-web:
	docker compose exec web sh
test:
	poetry run python manage.py test api

