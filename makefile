web:
	docker compose up  --build

dev:
	poetry run ./manage.py runserver