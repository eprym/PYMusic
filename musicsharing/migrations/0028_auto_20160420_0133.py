# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-20 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsharing', '0027_auto_20160417_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Gay', 'Gay'), ('Lesbian', 'Lesbian'), ('Bisexual', 'Bisexual'), ('Transgender', 'Transgender'), ('Undefined', 'undefined :)')], default='D', max_length=15),
        ),
    ]
