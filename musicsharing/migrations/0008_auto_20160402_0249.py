# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-02 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musicsharing', '0007_auto_20160402_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
