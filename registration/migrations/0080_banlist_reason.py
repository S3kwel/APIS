# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-12-14 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0079_pricelevel_isminor'),
    ]

    operations = [
        migrations.AddField(
            model_name='banlist',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]