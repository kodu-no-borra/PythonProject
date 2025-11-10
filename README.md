
# PythonProject

Проект на Django с Celery и PostgreSQL, запущенный через Docker Compose.
p.s. Извините, но мой боевой дух не позволил оставить мне как есть и я накидал еще поверх комиты с рефакторингом 🥹
Из за инициативы с докером немного просел по времени, но надеюсь это не повлияет на общую картину 🙈


## Требования

- Docker
- Docker Compose (v2, поддержка `docker compose`)
- Python 3.12 (локально для работы с Poetry, опционально)

## Быстрый старт

1. Клонируем репозиторий и переходим в директорию проекта:

```bash
git clone <repo_url>
cd PythonProject
````

2. Собираем контейнеры:

```bash
docker compose build
```

3. Запускаем контейнеры в фоновом режиме:

```bash
docker compose up -d
```

4. Проверяем, что все сервисы поднялись:

```bash
docker compose ps
```

Вы должны увидеть `web`, `celery`, `db` и `redis` со статусом `Up`.

## Первичная настройка Django

Заходим внутрь контейнера Django:

```bash
docker compose exec web bash
```

В контейнере выполняем миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

Создаем суперпользователя:

```bash
python manage.py createsuperuser
```

## Проверка работы Celery

1. Запускаем воркер Celery (если не запущен через docker-compose):

```bash
docker compose exec celery bash
celery -A __project__ worker --loglevel=info
```

2. Проверяем, что Celery подключился к Redis и готов принимать задачи.

## Настройка .env

Проект использует переменные окружения. Создайте файл `.env` в корне проекта:

```env
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_pass
POSTGRES_HOST=dev_postgres
POSTGRES_PORT=5432

CELERY_BROKER_URL=redis://dev_redis:6379/0
CELERY_RESULT_BACKEND=redis://dev_redis:6379/0
```

Django и Celery используют `os.getenv` для чтения этих переменных.

## Проверка API

После миграций можно создавать задачи через API:

```
POST http://localhost:8000/api/tasks/
Body (JSON):
{
  "title": "Первая задача",
  "description": "Описание для теста",
  "status": 1
}
```

## Остановка и удаление контейнеров

```bash
docker compose down
```

---
