# coding: utf-8
from __future__ import unicode_literals

from django.db import models
# from localflavor.us.models import USStateField
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _



# class WineQuerySet(models.QuerySet):
#     def in_cellar(self, arg=True):
#         return self.filter(date_opened__isnull=arg)

class Barcode(models.Model):
    code            = models.CharField(max_length=13, unique = True)
    date            = models.DateField(auto_now = True)

    def __unicode__(self):
        return self.code

class Address(models.Model):
    address_1 = models.CharField(_("address"), max_length=128, blank=True, null=True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True, null=True)
    city = models.CharField(_("city"), max_length=64, blank=True, null=True)
    zip_code = models.CharField(_("zip code"), max_length=5, blank=True, null=True)
    state = CountryField(blank=True, null=True)

    def __unicode__(self):
        return self.code

    def __str__(self):
        return address_1 + "\n" + address_2 + "\n" + city + "\n" + zip_code + "\n" + state

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
    # year = models.IntegerField()

    # A few more of these could be foreign keys. Keeping the data model simple
    # but might change because of wine laziness.

    winery = models.ForeignKey('Winery')
    importer = models.CharField(blank=True, null=True, max_length=50)
    notes = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to = 'wine/', blank=True, null=True)
    etiquette = models.ImageField(upload_to = 'wine/', blank=True, null=True)

    def __str__(self):
        return self.bottle_text

    def __unicode__(self):
        return "%s (%s)" % (self.bottle_text, self.year)

    # def in_cellar(self):
    #     """ For the admin display. """
    #     return not self.date_opened
    # in_cellar.boolean = True
    # in_cellar.short_description = _("In Cellar?")

    # objects = WineQuerySet.as_manager()

    # class Meta:
    #     ordering = ('-date_purchased',)


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
    address = models.ForeignKey(Address, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("wineries")


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, blank=True, null=True)

    def __str__(self):
        return self.name + " (" + self.address.city + ")"

    def __unicode__(self):
        return self.name
