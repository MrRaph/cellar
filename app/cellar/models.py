from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import string
from django.contrib.auth.models import User
from django.conf import settings

from wine.models import Wine

# Create your models here.
# class UserProfile(models.Model):
#     field = models.CharField(max_length=3)
#     user = models.OneToOneField(User)

USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local
_thread_locals = local()

def get_current_user():
    current_user = getattr(_thread_locals, USER_ATTR_NAME, None)
    return current_user() if current_user else current_user

class Cell(models.Model):
    zone = models.ForeignKey('Zone')
    wine = models.ForeignKey('wine.Wine', null=True, blank=True)

    row_number = models.IntegerField()
    col_number = models.IntegerField()

    def __str__(self):
        return self.getName()

    def getName(self):
        d = dict(enumerate(string.ascii_lowercase, 1))
        return d[self.col_number].upper() + str(self.row_number)

    def save(self, *args, **kw):
        zone = Zone.objects.all().filter(id=self.zone.id)
        if not self.row_number in range(1,zone[0].num_rows) and not self.col_number in range(1,zone[0].num_columns):
            print('Mauvaises valeurs ...')
        else:
            super(Cell, self).save(*args, **kw)

class Zone(models.Model):
    number = models.IntegerField(default=1)
    cellar = models.ForeignKey('Cellar')

    num_columns = models.IntegerField(default=1)
    num_rows = models.IntegerField(default=1)

    actual_temperature = models.IntegerField(
        default=15,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(5)
        ])

    def __unicode__(self):
        return self.cellar.name + " (" + str(self.number) + ")"

    def __str__(self):
        return self.cellar.name + " (" + str(self.number) + ")"

    def total_space(self):
        return self.num_columns * self.num_rows

    def get_used_space(self):
        used_space = 0
        for cell in Cell.objects.all().filter(zone__id=self.id):
            used_space += 1
        return used_space

    def get_free_space(self):
        used_space = 0
        for cell in Cell.objects.all().filter(zone__id=self.id):
            used_space += 1
        return self.total_space() - used_space

class Cellar(models.Model):
    name = models.CharField(max_length=100, default=_("My Cellar"))
    brand = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, default=get_current_user())
    number_of_zones = models.IntegerField(default=1)

    max_temperature = models.IntegerField(
        default=15,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(5)
        ])

    min_temperature = models.IntegerField(
        default=15,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(5)
        ])

    date_purchased = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def total_space(self):
        total_space = 0
        zones = Zone.objects.all().filter(cellar__id=self.id)
        if zones:
            for zone in zones:
                total_space += zone.total_space()
            return total_space
        else:
            return 0

    def total_free_space(self):
        total_free_space = 0
        zones = Zone.objects.all().filter(cellar__id=self.id)
        if zones:
            for zone in zones:
                total_free_space += zone.get_free_space()
            return total_free_space
        else:
            return 0

    def total_used_space(self):
        total_free_space = 0
        zones = Zone.objects.all().filter(cellar__id=self.id)
        if zones:
            for zone in zones:
                total_free_space += zone.get_free_space()
            return total_free_space
        else:
            return 0
