# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0004_auto_20160529_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grape',
            name='percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wine_type',
            field=models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Ros\xe9', 'Ros\xe9'), ('Orange', 'Orange'), ('Sparkling', 'Sparkling'), ('Fortified', 'Fortified'), ('Dessert', 'Desert')], max_length=10, verbose_name='Type'),
        ),
    ]