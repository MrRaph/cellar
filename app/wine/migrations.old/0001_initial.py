# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottle_text', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('date_purchased', models.DateField()),
                ('store', models.CharField(max_length=50)),
                ('importer', models.CharField(max_length=50)),
                ('date_consumed', models.DateField(blank=True, null=True)),
                ('liked_it', models.NullBooleanField()),
                ('notes', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Winery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='wine',
            name='winery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wine.Winery'),
        ),
        migrations.AddField(
            model_name='grape',
            name='wine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wine.Wine'),
        ),
    ]
