# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-30 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20170625_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='province',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='location.Province', verbose_name='省份'),
        ),
    ]