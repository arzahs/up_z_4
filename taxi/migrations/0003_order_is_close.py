# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_auto_20160624_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_close',
            field=models.BooleanField(default=False),
        ),
    ]
