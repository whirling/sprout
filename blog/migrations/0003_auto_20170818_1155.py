# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170817_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='self_health',
            field=models.BooleanField(default=False),
        ),
    ]