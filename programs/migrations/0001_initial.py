# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('invited_guests', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('flyer', models.ImageField(blank=True, upload_to='program-flyers')),
                ('venue', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
    ]
