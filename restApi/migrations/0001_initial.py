# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(default='', max_length=100)),
                ('longitud', models.CharField(default='', max_length=100)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('isEntrada', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('apellido', models.CharField(default='', max_length=100)),
                ('cedula', models.CharField(default='', max_length=100)),
                ('telefono', models.CharField(blank=True, default='', max_length=20)),
                ('faceData', models.CharField(default='', max_length=5000)),
            ],
            options={
                'ordering': ('apellido',),
            },
        ),
        migrations.AddField(
            model_name='asistencia',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApi.Operador'),
        ),
    ]
