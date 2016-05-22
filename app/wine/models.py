from __future__ import unicode_literals

from django.db import models


class Wine(models.Model):
    bottle_text = models.CharField(max_length=100)
    wine_type = models.CharField("Type", max_length=10) # Probably gonna make this a choices_list
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

    def __unicode__(self):
        return "%s (%s)" % (self.bottle_text, self.year)


class Grape(models.Model):
    wine = models.ForeignKey(Wine)
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=100)

    def __unicode__(self):
        return "%s (%s%%)" % (self.name, self.percentage)


class Winery(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "wineries"
