# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleWho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.AddField(
            model_name='memo',
            name='who',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docx.PeopleWho'),
        ),
    ]