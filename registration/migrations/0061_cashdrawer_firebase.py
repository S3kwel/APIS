# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-16 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0060_auto_20180315_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashdrawer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('action', models.CharField(max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tendered', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('user', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Firebase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]
