# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_auto_20170710_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='add_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2017, 7, 12, 10, 49, 2, 102569), verbose_name='活动时间'),
        ),
    ]