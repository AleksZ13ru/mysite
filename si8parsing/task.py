# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .code2 import findfile, parsing_si8

@shared_task
def add(x, y):
    return x + y


@shared_task
def find():
    return findfile()


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
