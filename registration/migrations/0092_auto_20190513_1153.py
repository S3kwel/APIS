# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0091_auto_20190513_1050'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='accommodationType',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='discord',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='division',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='roomateBlacklist',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='roommateRequests',
        ),
        migrations.AddField(
            model_name='staff',
            name='needRoom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='staff',
            name='specialSkills',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='telegram',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='staff',
            name='twitter',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='Division',
        ),
    ]
