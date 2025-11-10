FROM python:3.12-slim

WORKDIR /app

RUN mkdir -p media

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt update && \
    apt install -y gcc libpq-dev gettext nano tmux zsh git tree htop unzip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip --no-cache-dir && \
    pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-interaction --no-ansi

COPY . .

RUN poetry run python manage.py compilemessages -l ru -l en || echo "No messages to compile"

EXPOSE 8000
