# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_service_top'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='service',
            unique_together=set([('title', 'company')]),
        ),
    ]