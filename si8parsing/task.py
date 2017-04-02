# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .code2 import findfile, parsing_si8
from mysite.celery import app


@shared_task
def add(x, y):
    return x + y


@app.task
def find():
    findfile()


@app.task
def parsing(id):
    parsing_si8(id)


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
