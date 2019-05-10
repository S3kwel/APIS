# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0086_event_staffeventregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='staffEventRegistration',
            field=models.BooleanField(default=False, help_text='If on, staff will be allowed to register for the event at the same time that they enter in their staff info.', verbose_name='Allow staff to register for the event when they sign up as staff.'),
        ),
    ]
