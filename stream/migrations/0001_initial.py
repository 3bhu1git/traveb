# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=16)),
                ('createdon', models.IntegerField(max_length=16)),
                ('modifiedon', models.IntegerField(max_length=16)),
                ('fromlocation', models.CharField(max_length=256)),
                ('tolocation', models.CharField(max_length=256)),
                ('leavingon', models.IntegerField(max_length=16)),
                ('reachingon', models.IntegerField(max_length=16)),
                ('angel', models.CharField(max_length=64)),
                ('trustee', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[(0, 'ACTIVE'), (1, 'INACTIVE')], max_length=1)),
            ],
        ),
    ]
