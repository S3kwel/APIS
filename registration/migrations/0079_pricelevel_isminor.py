# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-01 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0078_priceleveloption_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelevel',
            name='isMinor',
            field=models.BooleanField(default=False),
        ),
    ]
