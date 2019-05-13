# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0082_auto_20181231_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dealerEmail',
            field=models.CharField(blank=True, default=b'registration@example.com', help_text='Email to display on error messages for dealer registration', max_length=200, verbose_name='Dealer Email'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registrationEmail',
            field=models.CharField(blank=True, default=b'registration@example.com', help_text='Email to display on error messages for attendee registration', max_length=200, verbose_name='Registration Email'),
        ),
        migrations.AlterField(
            model_name='event',
            name='staffEmail',
            field=models.CharField(blank=True, default=b'registration@example.com', help_text='Email to display on error messages for staff registration', max_length=200, verbose_name='Staff Email'),
        ),
    ]