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
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Cellar, Zone, Cell, Bottle
from .forms import CellarForm, ZoneForm, CellForm, BottleForm

## List Views

@login_required
def myCellars(request):
    cellars = Cellar.objects.all().filter(user=request.user)
    return render(request, 'list_cellars.html', {'cellars': cellars})

@login_required
def myZones(request):
    zones = Zone.objects.all().filter(cellar__user=request.user)
    return render(request, 'list_zones.html', {'zones': zones})

@login_required
def myCells(request):
    cells = Cell.objects.all().filter(zone__cellar__user=request.user)
    return render(request, 'list_cells.html', {'cells': cells})

@login_required
def myBottles(request):
    bottles = Bottle.objects.all().filter(cell__zone__cellar__user=request.user) | Bottle.objects.all().filter(user=request.user)
    return render(request, 'list_bottles.html', {'bottles': bottles})

## Detail Views

@login_required
def cellarDetail(request, id):
    cellars = Cellar.objects.all().filter(user=request.user, id=id)
    return render(request, 'list_cellars.html', {'cellars': cellars})

@login_required
def zoneDetail(request, id):
    zones = Zone.objects.all().filter(cellar__user=request.user, id=id)
    return render(request, 'list_zones.html', {'zones': zones})

@login_required
def cellDetail(request, id):
    cells = Cell.objects.all().filter(zone__cellar__user=request.user, id=id)
    return render(request, 'list_cells.html', {'cells': cells})

@login_required
def bottleDetail(request, id):
    bottles = Bottle.objects.all().filter(user=request.user, id=id)
    return render(request, 'list_bottles.html', {'bottles': bottles})

## Delete Views

@login_required
def cellarDelete(request, id):
    cellars = Cellar.objects.all().filter(user=request.user, id=id).delete()
    # return render(request, 'list_cellars.html', {'cellars': cellars})
    return myCellars(request)

@login_required
def zoneDelete(request, id):
    zones = Zone.objects.all().filter(cellar__user=request.user, id=id).delete()
    # return render(request, 'list_zones.html', {'zones': zones})
    return myZones(request)

@login_required
def cellDelete(request, id):
    cells = Cell.objects.all().filter(zone__cellar__user=request.user, id=id).delete()
    # return render(request, 'list_cells.html', {'cells': cells})
    return myCells(request)

@login_required
def bottleDelete(request, id):
    bottles = Bottle.objects.all().filter(user=request.user, id=id).delete()
    # return render(request, 'list_bottles.html', {'bottles': bottles})
    return myBottles(request)


## Edit Views

@login_required
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

@login_required
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

@login_required
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

@login_required
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
