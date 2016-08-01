# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0012_auto_20160801_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='city',
        ),
        migrations.RemoveField(
            model_name='store',
            name='state',
        ),
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.Address'),
        ),
    ]
