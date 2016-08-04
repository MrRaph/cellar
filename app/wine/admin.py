from django.contrib import admin

from .models import Wine, Grape, Winery, Store, Address, Barcode
from django.utils.translation import gettext_lazy as _

class GrapeInline(admin.TabularInline):
    model = Grape
    extra = 0


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ["__str__", "wine_type", ]
    fieldsets = (
        (_('Bottle'), {
            'fields': ('bottle_text', 'wine_type', 'winery', 'image', 'etiquette', ),
            }),
    )

    inlines = [
        GrapeInline,
    ]


admin.site.register(Winery)
admin.site.register(Store)
admin.site.register(Address)
admin.site.register(Barcode)
