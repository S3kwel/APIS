# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-20 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0087_auto_20190318_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='accommodationType',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='roomateBlacklist',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='staff',
            name='roommateRequests',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
