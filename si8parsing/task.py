
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from .code2 import findfile, parsing_si8

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skabel.settings')

app = Celery('skabel', result='redis://localhost', broker='redis://localhost:6379/0')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# для запуска
# C:\Python\env\twoenv\Scripts\activate
# D:
# cd D:\IdeaProjects\prj\skabel
# C:\Python\env\twoenv\Scripts\celery -A skabel beat -l info -S django


@app.task(bind=True)
def findfile_si8(self):
        print('Hello-------')
        #findfile.delay()


@app.task(bind=True)
def parsing_si8():
    # parsing_si8()
    pass

