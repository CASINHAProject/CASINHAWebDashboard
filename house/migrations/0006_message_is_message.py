# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_message_crated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_message',
            field=models.BooleanField(default=False),
        ),
    ]
