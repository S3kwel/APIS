# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0083_auto_20190507_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='charity',
        ),
        migrations.RemoveField(
            model_name='event',
            name='dealerDiscount',
        ),
        migrations.RemoveField(
            model_name='event',
            name='dealerEmail',
        ),
        migrations.RemoveField(
            model_name='event',
            name='dealerRegEnd',
        ),
        migrations.RemoveField(
            model_name='event',
            name='dealerRegStart',
        ),
        migrations.RemoveField(
            model_name='event',
            name='newStaffDiscount',
        ),
        migrations.RemoveField(
            model_name='event',
            name='staffDiscount',
        ),
        migrations.AddField(
            model_name='event',
            name='useAuthToken',
            field=models.BooleanField(default=False, help_text='Toggle this setting off if you would like anyone with the staff registration URL to be able to sign up.', verbose_name='Use Auth Tokens'),
        ),
    ]