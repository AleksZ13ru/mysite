# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('starttime', models.TimeField()),
                ('stoptime', models.TimeField()),
            ],
            options={
                'verbose_name': 'Описание смены',
                'verbose_name_plural': 'Описание смен',
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(blank=True, null=True)),
                ('fileurl', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('план', 'план'), ('факт', 'факт')], max_length=4)),
                ('year', models.IntegerField()),
                ('startday', models.DateField()),
                ('lenght', models.IntegerField(default=14)),
                ('stopday', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Отпуск',
                'verbose_name_plural': 'Отпуска',
            },
        ),
        migrations.CreateModel(
            name='MicroSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startday', models.DateField()),
                ('lenght', models.IntegerField(default=14)),
                ('stopday', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Подмена',
                'verbose_name_plural': 'Подмена',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=30)),
                ('secondname', models.CharField(blank=True, max_length=30, null=True)),
                ('birtday', models.DateField(blank=True, null=True)),
                ('dayofwork', models.DateField(blank=True, null=True)),
                ('dayofquit', models.DateField(blank=True, null=True)),
                ('telefon', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Function')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=150)),
                ('startday', models.DateField()),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'Графики работы',
            },
        ),
        migrations.CreateModel(
            name='Weekend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('Выходной', 'Выходной'), ('Отгул', 'Отгул'), ('Без содержания', 'Без содержания')], max_length=16)),
                ('motive', models.CharField(choices=[('Служеб.', 'Служебное задание'), ('Семейн.', 'Семейные обстоятельства'), ('Другое ', 'Другое')], max_length=8)),
                ('datestart', models.DateField()),
                ('timestart', models.TimeField()),
                ('stoptime', models.TimeField()),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.People')),
            ],
            options={
                'verbose_name': 'Отгулы и выходные',
                'verbose_name_plural': 'Отгулы и выходные',
            },
        ),
        migrations.AddField(
            model_name='people',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dept.Schedule'),
        ),
        migrations.AddField(
            model_name='microschedule',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.People'),
        ),
        migrations.AddField(
            model_name='microschedule',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Schedule'),
        ),
        migrations.AddField(
            model_name='holiday',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.People'),
        ),
        migrations.AddField(
            model_name='change',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Schedule'),
        ),
    ]
