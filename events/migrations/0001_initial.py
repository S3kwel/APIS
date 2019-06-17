# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-17 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('r18', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('time_start', models.DateTimeField()),
                ('duration', models.IntegerField(choices=[(30, '30 Minutes'), (60, '1 Hour'), (90, '1.5 Hours'), (120, '2 Hours'), (150, '2.5 Hours'), (180, '3 Hours'), (210, '3.5 Hours'), (240, '4 Hours'), (270, '4.5 Hours'), (300, '5 Hours'), (330, '5.5 Hours'), (360, '6 Hours'), (390, '6.5 Hours'), (420, '7 Hours'), (450, '7.5 Hours'), (480, '8 Hours'), (510, '8.5 Hours'), (540, '9 Hours'), (570, '9.5 Hours'), (600, '10 Hours'), (630, '10.5 Hours'), (660, '11 Hours'), (690, '11.5 Hours'), (720, '12 Hours'), (750, '12.5 Hours'), (780, '13 Hours'), (810, '13.5 Hours'), (840, '14 Hours'), (870, '14.5 Hours'), (900, '15 Hours'), (930, '15.5 Hours'), (960, '16 Hours'), (990, '16.5 Hours'), (1020, '17 Hours'), (1050, '17.5 Hours'), (1080, '18 Hours'), (1110, '18.5 Hours'), (1140, '19 Hours'), (1170, '19.5 Hours'), (1200, '20 Hours'), (1230, '20.5 Hours'), (1260, '21 Hours'), (1290, '21.5 Hours'), (1320, '22 Hours'), (1350, '22.5 Hours'), (1380, '23 Hours'), (1410, '23.5 Hours'), (1440, '24 Hours')], default=60)),
                ('type', models.IntegerField(choices=[(0, 'Panel'), (1, 'Blackout'), (2, 'Convention Event'), (3, 'Convention Ops')], default=0)),
                ('setup_time', models.IntegerField(choices=[(0, 'No Setup Time'), (15, '15 Minutes'), (30, '30 Minutes'), (60, '1 Hour'), (90, '1.5 Hours'), (120, '2 Hours'), (150, '2.5 Hours'), (180, '3 Hours')], default=30)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='PanelComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_to_panelist', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Panel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Panelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('fan_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('checked_in', models.BooleanField(default=False)),
                ('checked_in_date', models.DateTimeField(blank=True, null=True)),
                ('badge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Badge')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='PanelRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='PanelRequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_type', models.IntegerField(choices=[(0, 'Panel'), (1, 'Blackout'), (2, 'Convention Event'), (3, 'Convention Ops')], default=0)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='PanelSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=20, null=True)),
                ('setup_notes', models.TextField(blank=True, null=True)),
                ('time_start', models.DateTimeField()),
                ('duration', models.IntegerField(choices=[(15, '0 Hours, 15 Minutes'), (30, '0 Hours, 30 Minutes'), (45, '0 Hours, 45 Minutes'), (60, '1 Hour, 0 Minutes'), (75, '1 Hour, 15 Minutes'), (90, '1 Hour, 30 Minutes'), (105, '1 Hour, 45 Minutes'), (120, '2 Hours, 0 Minutes'), (135, '2 Hours, 15 Minutes'), (150, '2 Hours, 30 Minutes'), (165, '2 Hours, 45 Minutes'), (180, '3 Hours, 0 Minutes'), (195, '3 Hours, 15 Minutes'), (210, '3 Hours, 30 Minutes'), (225, '3 Hours, 45 Minutes'), (240, '4 Hours, 0 Minutes'), (255, '4 Hours, 15 Minutes'), (270, '4 Hours, 30 Minutes'), (285, '4 Hours, 45 Minutes'), (300, '5 Hours, 0 Minutes'), (315, '5 Hours, 15 Minutes'), (330, '5 Hours, 30 Minutes'), (345, '5 Hours, 45 Minutes'), (360, '6 Hours, 0 Minutes'), (375, '6 Hours, 15 Minutes'), (390, '6 Hours, 30 Minutes'), (405, '6 Hours, 45 Minutes'), (420, '7 Hours, 0 Minutes'), (435, '7 Hours, 15 Minutes'), (450, '7 Hours, 30 Minutes'), (465, '7 Hours, 45 Minutes'), (480, '8 Hours, 0 Minutes'), (495, '8 Hours, 15 Minutes'), (510, '8 Hours, 30 Minutes'), (525, '8 Hours, 45 Minutes'), (540, '9 Hours, 0 Minutes'), (555, '9 Hours, 15 Minutes'), (570, '9 Hours, 30 Minutes'), (585, '9 Hours, 45 Minutes'), (600, '10 Hours, 0 Minutes'), (615, '10 Hours, 15 Minutes'), (630, '10 Hours, 30 Minutes'), (645, '10 Hours, 45 Minutes'), (660, '11 Hours, 0 Minutes'), (675, '11 Hours, 15 Minutes'), (690, '11 Hours, 30 Minutes'), (705, '11 Hours, 45 Minutes'), (720, '12 Hours, 0 Minutes'), (735, '12 Hours, 15 Minutes'), (750, '12 Hours, 30 Minutes'), (765, '12 Hours, 45 Minutes'), (780, '13 Hours, 0 Minutes'), (795, '13 Hours, 15 Minutes'), (810, '13 Hours, 30 Minutes'), (825, '13 Hours, 45 Minutes'), (840, '14 Hours, 0 Minutes'), (855, '14 Hours, 15 Minutes'), (870, '14 Hours, 30 Minutes'), (885, '14 Hours, 45 Minutes'), (900, '15 Hours, 0 Minutes'), (915, '15 Hours, 15 Minutes'), (930, '15 Hours, 30 Minutes'), (945, '15 Hours, 45 Minutes'), (960, '16 Hours, 0 Minutes'), (975, '16 Hours, 15 Minutes'), (990, '16 Hours, 30 Minutes'), (1005, '16 Hours, 45 Minutes'), (1020, '17 Hours, 0 Minutes'), (1035, '17 Hours, 15 Minutes'), (1050, '17 Hours, 30 Minutes'), (1065, '17 Hours, 45 Minutes'), (1080, '18 Hours, 0 Minutes'), (1095, '18 Hours, 15 Minutes'), (1110, '18 Hours, 30 Minutes'), (1125, '18 Hours, 45 Minutes'), (1140, '19 Hours, 0 Minutes'), (1155, '19 Hours, 15 Minutes'), (1170, '19 Hours, 30 Minutes'), (1185, '19 Hours, 45 Minutes'), (1200, '20 Hours, 0 Minutes'), (1215, '20 Hours, 15 Minutes'), (1230, '20 Hours, 30 Minutes'), (1245, '20 Hours, 45 Minutes'), (1260, '21 Hours, 0 Minutes'), (1275, '21 Hours, 15 Minutes'), (1290, '21 Hours, 30 Minutes'), (1305, '21 Hours, 45 Minutes'), (1320, '22 Hours, 0 Minutes'), (1335, '22 Hours, 15 Minutes'), (1350, '22 Hours, 30 Minutes'), (1365, '22 Hours, 45 Minutes'), (1380, '23 Hours, 0 Minutes'), (1395, '23 Hours, 15 Minutes'), (1410, '23 Hours, 30 Minutes'), (1425, '23 Hours, 45 Minutes'), (1440, '24 Hours, 0 Minutes'), (1455, '24 Hours, 15 Minutes'), (1470, '24 Hours, 30 Minutes'), (1485, '24 Hours, 45 Minutes')], default=60)),
                ('setup_time', models.IntegerField(choices=[(0, 'No Setup Time'), (15, '15 Minutes'), (30, '30 Minutes'), (60, '1 Hour'), (90, '1.5 Hours'), (120, '2 Hours'), (150, '2.5 Hours'), (180, '3 Hours')], default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
                ('panel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('color', models.CharField(default='#', max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='panelslot',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Room'),
        ),
        migrations.AddField(
            model_name='panelrequest',
            name='request_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.PanelRequestType'),
        ),
        migrations.AddField(
            model_name='panel',
            name='panelist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Panelist'),
        ),
        migrations.AddField(
            model_name='panel',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Room'),
        ),
        migrations.AddField(
            model_name='panel',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Track'),
        ),
    ]
