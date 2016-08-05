from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Cellar, Zone, Cell, Bottle

@admin.register(Cellar)
class CellarAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_purchased", 'total_space', 'user' ]
    fieldsets = (
        (_('Infos'), {
            'fields': (
                'name', 'date_purchased', 'brand',
                'max_temperature', 'min_temperature', 'user',
            ),
            }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

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
    # list_display = ["__str__", "zone", "row_number", "col_number", "wine", ]
    list_display = ["__str__", "zone", "row_number", "col_number", ]
    fieldsets = (
        (_('Infos'), {
            # 'fields': ('zone', 'row_number', 'col_number', 'wine',),
            'fields': ('zone', 'row_number', 'col_number', ),
            }),
    )

@admin.register(Bottle)
class BottleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "wine", "cell", "user", "liked_it" ]
    fieldsets = (
        (_('Infos'), {
            'fields': ('wine', "cell", 'user', 'liked_it'),
            }),
    )
