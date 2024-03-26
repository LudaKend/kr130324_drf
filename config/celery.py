from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# установка переменной окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# создание экземпляра объекта Celery
app = Celery('habits')

# загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# автоматическое обнаружение и регистрация задач из файлов
# tasks.py в приложениях Django
app.autodiscover_tasks()
