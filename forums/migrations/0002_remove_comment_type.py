# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='type',
        ),
    ]
