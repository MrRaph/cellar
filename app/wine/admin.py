from django.contrib import admin

from .models import Wine, Grape, Winery

class GrapeInline(admin.TabularInline):
    model = Grape


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Bottle', {
            'fields': ('bottle_text', 'year', 'wine_type', 'winery',),
            }),
        ('Purchase', {
            'fields': ('date_purchased', 'store', 'importer'),
            }),
        ('Consumption', {
            'fields': ('date_consumed', 'liked_it', 'notes',),
            })
    )

    inlines = [
        GrapeInline,
    ]


admin.site.register(Winery)
