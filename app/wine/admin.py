from django.contrib import admin

from .models import Wine, Grape, Winery, Store

class GrapeInline(admin.TabularInline):
    model = Grape
    extra = 0


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ["__str__", "year", "wine_type", "in_cellar",]
    fieldsets = (
        ('Bottle', {
            'fields': ('bottle_text', 'year', 'wine_type', 'winery',),
            }),
        ('Purchase', {
            'fields': ('date_purchased', 'price', 'store', 'importer'),
            }),
        ('Consumption', {
            'fields': ('date_opened', 'date_finished', 'liked_it', 'notes',),
            })
    )

    inlines = [
        GrapeInline,
    ]


admin.site.register(Winery)
admin.site.register(Store)
