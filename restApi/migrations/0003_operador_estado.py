# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0002_tipousuario_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='operador',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=3),
        ),
    ]