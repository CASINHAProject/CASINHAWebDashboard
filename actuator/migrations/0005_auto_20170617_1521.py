# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actuator', '0004_auto_20170612_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actuators', to='house.House', verbose_name='Casa correspondente'),
        ),
    ]
