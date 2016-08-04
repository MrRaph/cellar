from django import forms
from django.utils.translation import ugettext as _

from .models import Wine, Store, Barcode, Address, Grape, Winery

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', ]

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine

        fields = ['bottle_text', 'wine_type', 'winery', 'importer', 'notes', 'image', 'etiquette', ]

class BarcodeForm(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = ['code', ]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_1', 'address_2', 'city', 'zip_code', 'state' ]

class GrapeForm(forms.ModelForm):
    class Meta:
        model = Grape
        fields = ['wine', 'name', 'percentage', ]

class WineryForm(forms.ModelForm):
    class Meta:
        model = Winery
        exclude =('address',)
