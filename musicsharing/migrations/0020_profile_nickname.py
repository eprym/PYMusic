# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-07 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsharing', '0019_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
