import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '__project__.settings')

app = Celery('__project__')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
