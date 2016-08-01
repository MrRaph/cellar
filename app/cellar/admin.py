from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Cellar, Zone

@admin.register(Cellar)
class CellarAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "date_purchased",]
    fieldsets = (
        (_('Infos'), {
            'fields': ('name', 'date_purchased', 'brand',),
            }),
    )

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ["__str__", "cellar",]
    fieldsets = (
        (_('Infos'), {
            'fields': ('number', 'cellar',),
            }),
    )
