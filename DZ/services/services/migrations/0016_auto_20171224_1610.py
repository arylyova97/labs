# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 13:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20171223_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='odate',
            field=models.DateField(default=datetime.datetime(2017, 12, 24, 16, 10, 37, 428151)),
        ),
    ]
