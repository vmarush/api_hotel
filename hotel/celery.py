import os
from celery import Celery

# from celery.schedules import crontab
# import django_celery_beat


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel.settings")

app = Celery("hotel", include=["rooms.tasks"])
app.config_from_object("django.conf:settings", namespace="CELERY")

# import processes.tasks

app.autodiscover_tasks()