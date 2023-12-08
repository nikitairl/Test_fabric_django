import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disptacher.settings')

app = Celery('disptacher')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
