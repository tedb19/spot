# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20160619_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='environment',
        ),
    ]
