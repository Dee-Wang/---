# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-16 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default=' ', max_length=32, verbose_name='城市名称')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(default=' ', max_length=32, verbose_name='省份名称')),
            ],
            options={
                'verbose_name': '省份',
                'verbose_name_plural': '省份',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(default=' ', max_length=64, verbose_name='店铺名称')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='具体地址')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.City', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '店铺',
                'verbose_name_plural': '店铺',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Province', verbose_name='省份'),
        ),
    ]