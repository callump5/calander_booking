# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_session_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='description',
            field=models.TextField(default='sdg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='image',
            field=models.ImageField(default='qwf', upload_to=b'images'),
            preserve_default=False,
        ),
    ]
