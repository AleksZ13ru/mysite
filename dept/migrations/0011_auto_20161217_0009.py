# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0010_auto_20161217_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.People'),
        ),
    ]
