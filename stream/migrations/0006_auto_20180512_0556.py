# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-12 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0005_auto_20180510_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='leavingon',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='trips',
            name='reachingon',
            field=models.CharField(max_length=64),
        ),
    ]
