# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0004_auto_20161216_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='birtday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='dayofwork',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='holiday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dept.Holiday'),
        ),
        migrations.AlterField(
            model_name='people',
            name='secondname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='telefon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
