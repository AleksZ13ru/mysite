# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docx', '0003_auto_20170824_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memo',
            name='event',
        ),
        migrations.RemoveField(
            model_name='memo',
            name='note',
        ),
        migrations.AddField(
            model_name='event',
            name='memo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='docx.Memo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='memo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='docx.Memo'),
            preserve_default=False,
        ),
    ]
