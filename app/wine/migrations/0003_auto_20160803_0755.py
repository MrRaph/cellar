# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0002_auto_20160801_1247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wine',
            options={},
        ),
        migrations.RemoveField(
            model_name='wine',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='date_finished',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='date_opened',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='date_purchased',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='liked_it',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='price',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='store',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='year',
        ),
    ]