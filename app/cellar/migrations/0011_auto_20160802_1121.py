# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0010_cellar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellar',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
