from __future__ import unicode_literals

from django.db import models


class Wine(models.Model):
    bottle_text = models.CharField(max_length=100)
    year = models.IntegerField()

    date_purchased = models.DateField()

    # A few more of these could be foreign keys. Keeping the data model simple
    # but might change because of wine laziness.
    store = models.CharField(max_length=50)
    winery = models.ForeignKey('Winery')
    importer = models.CharField(max_length=50)

    date_consumed = models.DateField(blank=True, null=True)
    liked_it = models.NullBooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, default="")


class Grape(models.Model):
    wine = models.ForeignKey(Wine)
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=100)


class Winery(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "wineries"
