# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 21:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_auto_20181013_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.DateField(verbose_name='Booking date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(choices=[(datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM'), (datetime.time(13, 0), '1 PM'), (datetime.time(14, 0), '2 PM'), (datetime.time(15, 0), '3 PM'), (datetime.time(16, 0), '4 PM'), (datetime.time(17, 0), '5 PM')], max_length=200, verbose_name='Booking time'),
        ),
    ]