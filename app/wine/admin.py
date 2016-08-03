from django.contrib import admin

from .models import Wine, Grape, Winery, Store
from django.utils.translation import gettext_lazy as _

class GrapeInline(admin.TabularInline):
    model = Grape
    extra = 0


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    # list_display = ["__str__", "year", "wine_type", "in_cellar",]
    # list_display = ["__str__", "year", "wine_type", ]
    list_display = ["__str__", "wine_type", ]
    fieldsets = (
        (_('Bottle'), {
            'fields': ('bottle_text', 'wine_type', 'winery',),
            }),
        # (_('Purchase'), {
        #     'fields': ('date_purchased', 'price', 'store', 'importer'),
        #     }),
        # (_('Consumption'), {
        #     'fields': ('date_opened', 'date_finished', 'liked_it', 'notes',),
        #     })
    )

    inlines = [
        GrapeInline,
    ]


admin.site.register(Winery)
admin.site.register(Store)
