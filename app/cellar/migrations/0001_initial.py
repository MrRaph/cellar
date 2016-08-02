# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cellar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='My Cellar', max_length=100)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('date_purchased', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('cellar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellar.Cellar')),
            ],
        ),
    ]