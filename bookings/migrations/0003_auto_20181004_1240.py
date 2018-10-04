# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20181003_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.CharField(choices=[(1, b'9:00 am'), (2, b'10:00 am'), (3, b'11:00 am'), (4, b'12:00 am'), (5, b'1:00 pm')], help_text=b'Booking slot', max_length=200, verbose_name='Booking slot'),
        ),
    ]