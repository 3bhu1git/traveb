# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-12 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0007_auto_20180512_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips',
            name='gid',
        ),
    ]
