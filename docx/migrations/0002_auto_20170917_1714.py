# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docx', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memostatus',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterField(
            model_name='memostatus',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
