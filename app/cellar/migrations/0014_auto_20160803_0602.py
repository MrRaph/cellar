# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0013_bottle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='wine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cellar.Bottle'),
        ),
    ]
