from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Cellar, Zone, Cell

@admin.register(Cellar)
class CellarAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_purchased", 'total_space', ]
    fieldsets = (
        (_('Infos'), {
            'fields': ('name', 'date_purchased', 'brand', 'max_temperature', 'min_temperature',),
            }),
    )

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ["__str__", "cellar", "total_space", ]
    fieldsets = (
        (_('Infos'), {
            'fields': ('number', 'cellar', 'actual_temperature', 'num_columns', 'num_rows',),
            }),
    )

@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ["__str__", "zone", "row_number", "col_number", "wine", ]
    fieldsets = (
        (_('Infos'), {
            'fields': ('zone', 'row_number', 'col_number', 'wine',),
            }),
    )
