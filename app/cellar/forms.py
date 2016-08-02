from django import forms
from django.utils.translation import ugettext as _

from .models import Cellar, Zone, Cell

class CellarForm(forms.ModelForm):
    class Meta:
        model = Cellar
        fields = ['name', 'brand', 'max_temperature', 'min_temperature', 'number_of_zones', ]

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['number', 'cellar', 'num_columns', 'num_rows', 'actual_temperature', ]

class CellForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = ['zone', 'wine', 'row_number', 'col_number', ]
