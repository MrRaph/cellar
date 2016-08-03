# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-02 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0002_auto_20160801_1247'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cellar', '0012_auto_20160802_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wine.Wine')),
            ],
        ),
    ]
