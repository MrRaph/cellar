from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login
from datetime import timedelta
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
# from django.db.models import Q

# Create your views here.
from .models import Cellar, Zone, Cell, Bottle
from .forms import CellarForm, ZoneForm, CellForm, BottleForm

## List Views

def myCellars(request):
    cellars = Cellar.objects.all().filter(user=request.user)
    return render(request, 'list_cellars.html', {'cellars': cellars})

def myZones(request):
    zones = Zone.objects.all().filter(cellar__user=request.user)
    return render(request, 'list_zones.html', {'zones': zones})

def myCells(request):
    cells = Cell.objects.all().filter(zone__cellar__user=request.user)
    return render(request, 'list_cells.html', {'cells': cells})

def myBottles(request):
    bottles = Bottle.objects.all().filter(cell__zone__cellar__user=request.user) | Bottle.objects.all().filter(user=request.user)
    return render(request, 'list_bottles.html', {'bottles': bottles})
## Detail Views

def cellarDetail(request, id):
    cellars = Cellar.objects.all().filter(user=request.user, id=id)
    return render(request, 'list_cellars.html', {'cellars': cellars})

def zoneDetail(request, id):
    zones = Zone.objects.all().filter(cellar__user=request.user, id=id)
    return render(request, 'list_zones.html', {'zones': zones})

def cellDetail(request, id):
    cells = Cell.objects.all().filter(zone__cellar__user=request.user, id=id)
    return render(request, 'list_cells.html', {'cells': cells})

def bottleDetail(request, id):
    bottles = Bottle.objects.all().filter(user=request.user, id=id)
    return render(request, 'list_bottles.html', {'bottles': bottles})

## Edit Views

def editCellar(request, id=None):
    # cellar = get_object_or_404(Cellar, id=id)

    try:
        cellar = Cellar.objects.get(id=id)
    except:
        cellar = None

    form = CellarForm(request.POST or None, instance=cellar)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return HttpResponseRedirect('/cellar/cellars/')
    return render(request, 'edit_cellar.html', {'form': form})

def editZone(request, id=None):
    # zone = get_object_or_404(Zone, id=id)

    try:
        zone = Zone.objects.get(id=id)
    except:
        zone = None

    form = ZoneForm(request.POST or None, instance=zone)
    form.fields['cellar'].queryset = Cellar.objects.filter(user=request.user)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('/cellar/zones/')
    return render(request, 'edit_zone.html', {'form': form})

def editCell(request, id=None):
    # cell = get_object_or_404(Cell, id=id)

    try:
        cell = Cell.objects.get(id=id)
    except:
        cell = None

    form = CellForm(request.POST or None, instance=cell)
    form.fields['zone'].queryset = Zone.objects.filter(cellar__user=request.user)
    # form.fields['wine'].queryset = Zone.objects.filter(cellar__user=request.user)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('/cellar/cells/')
    return render(request, 'edit_cell.html', {'form': form})

def editBottle(request, id=None):
    # cellar = get_object_or_404(Cellar, id=id)

    try:
        bottle = Bottle.objects.get(id=id)
    except:
        bottle = None

    form = BottleForm(request.POST or None, instance=bottle)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return HttpResponseRedirect('/cellar/bottles/')
    return render(request, 'edit_bottle.html', {'form': form})
