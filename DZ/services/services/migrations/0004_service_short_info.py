# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20171217_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='short_info',
            field=models.TextField(default=''),
        ),
    ]
