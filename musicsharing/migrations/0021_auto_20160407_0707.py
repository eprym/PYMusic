# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-07 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsharing', '0020_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='profile_image/bg.jpg', upload_to='profile_image'),
        ),
    ]