# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20180409_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
