# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=128, null=True, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=128, null=True, verbose_name="address cont'd")),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='city')),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='zip code')),
                ('state', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=13, unique=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottle_text', models.CharField(max_length=100)),
                ('wine_type', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Rosé', 'Rosé'), ('Orange', 'Orange'), ('Sparkling', 'Sparkling'), ('Fortified', 'Fortified'), ('Dessert', 'Dessert')], max_length=10, verbose_name='Type')),
                ('year', models.IntegerField()),
                ('date_purchased', models.DateField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('importer', models.CharField(blank=True, max_length=50, null=True)),
                ('date_opened', models.DateField(blank=True, null=True)),
                ('date_finished', models.DateField(blank=True, null=True)),
                ('liked_it', models.NullBooleanField()),
                ('notes', models.TextField(blank=True, default='')),
                ('barcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.Barcode')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.Store')),
            ],
            options={
                'ordering': ('-date_purchased',),
            },
        ),
        migrations.CreateModel(
            name='Winery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wine.Address')),
            ],
            options={
                'verbose_name_plural': 'wineries',
            },
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