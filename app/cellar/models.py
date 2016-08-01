from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Zone(models.Model):
    number = models.IntegerField(default=1)
    cellar = models.ForeignKey('Cellar')

    def __unicode__(self):
        return self.cellar.name + " (" + str(self.number) + ")"

    def __str__(self):
        return self.cellar.name + " (" + str(self.number) + ")"

class Cellar(models.Model):
    name = models.CharField(max_length=100, default="My Cellar")
    brand = models.CharField(max_length=100, blank=True, null=True)

    date_purchased = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
