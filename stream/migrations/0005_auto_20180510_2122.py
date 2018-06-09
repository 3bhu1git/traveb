# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_trips_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='createdon',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='trips',
            name='gid',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='trips',
            name='leavingon',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='trips',
            name='modifiedon',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='trips',
            name='reachingon',
            field=models.CharField(max_length=16),
        ),
    ]
