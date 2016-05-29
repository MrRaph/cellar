# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 19:10
from __future__ import unicode_literals

from django.db import migrations


def migrate_store_to_fk(apps, schema_editor):
    Wine = apps.get_model('wine', 'Wine')
    Store = apps.get_model('wine', 'Store')

    wines = Wine.objects.all()
    for wine in wines:
        store, _ = Store.objects.get_or_create(name=wine.store)
        wine.store_fk = store
        wine.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0006_auto_20160529_1910'),
    ]

    operations = [
        migrations.RunPython(migrate_store_to_fk)
    ]