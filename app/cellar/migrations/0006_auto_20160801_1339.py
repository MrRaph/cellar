# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0005_auto_20160801_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='num_columns',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='zone',
            name='num_rows',
            field=models.IntegerField(default=1),
        ),
    ]
