# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 09:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0017_auto_20160803_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='date_purchased',
            field=models.DateField(default=datetime.date(2016, 8, 4)),
        ),
    ]
