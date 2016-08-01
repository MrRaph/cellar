# coding: utf-8
from __future__ import unicode_literals

from django.db import models
# from localflavor.us.models import USStateField
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _



class WineQuerySet(models.QuerySet):
    def in_cellar(self, arg=True):
        return self.filter(date_opened__isnull=arg)

class Barcode(models.Model):
    code            = models.CharField(max_length=13, unique = True)
    date            = models.DateField(auto_now = True)

    def __unicode__(self):
        return self.code

class Wine(models.Model):
    # Adapted from: https://en.wikipedia.org/wiki/Outline_of_wine#Types_of_wine
    WINE_TYPES = (
        ("Red", _("Red")),
        ("White", _("White")),
        ("Rosé", _("Rosé")),
        ("Orange", _("Orange")),
        ("Sparkling", _("Sparkling")),
        ("Fortified", _("Fortified")),
        ("Dessert", _("Dessert"))
    )

    bottle_text = models.CharField(max_length=100)
    wine_type = models.CharField("Type", max_length=10, choices=WINE_TYPES)
    year = models.IntegerField()

    date_purchased = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=4, blank=True,
                                null=True)

    # A few more of these could be foreign keys. Keeping the data model simple
    # but might change because of wine laziness.
    store = models.ForeignKey('Store', blank=True, null=True)
    winery = models.ForeignKey('Winery')
    importer = models.CharField(blank=True, null=True, max_length=50)
    barcode = models.ForeignKey('Barcode', blank=True, null=True)

    date_opened = models.DateField(blank=True, null=True)
    date_finished = models.DateField(blank=True, null=True)
    liked_it = models.NullBooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, default="")

    def __str__(self):
        return self.bottle_text

    def __unicode__(self):
        return "%s (%s)" % (self.bottle_text, self.year)

    def in_cellar(self):
        """ For the admin display. """
        return not self.date_opened
    in_cellar.boolean = True
    in_cellar.short_description = _("In Cellar?")

    objects = WineQuerySet.as_manager()

    class Meta:
        ordering = ('-date_purchased',)


class Grape(models.Model):
    wine = models.ForeignKey(Wine)
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "%s (%s%%)" % (self.name, self.percentage)


class Winery(models.Model):
    name = models.CharField(max_length=50)
    country = CountryField(blank=True)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("wineries")


class Store(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, default="")
    # state = USStateField(blank=True)
    state = CountryField(blank=True)

    def __str__(self):
        return self.name + " (" + self.city + ")"

    def __unicode__(self):
        return self.name
