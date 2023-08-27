from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

# import django_celery_beat

__all__ = ("celery_app",)