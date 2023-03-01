import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Exception_Handling_2023.settings')
celery_app = Celery('Exception_Handling_2023')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()