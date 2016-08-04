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
from django.forms import inlineformset_factory


# Create your views here.
from .models import Wine, Store, Barcode, Address, Grape, Winery
from .forms import WineForm, StoreForm, BarcodeForm, AddressForm, AddressForm, GrapeForm, WineryForm

from cellar.models import Bottle

## List Views

def allWines(request):
    wines = Wine.objects.all()
    return render(request, 'list_wines.html', {'wines': wines})

def allWineries(request):
    wineries = Winery.objects.all()
    return render(request, 'list_wineries.html', {'wineries': wineries})

## Detail Views

def wineDetail(request, id):
    wines = Wine.objects.all().filter(id=id)
    # wineries = Winery.objects.all().filter()
    liked = Bottle.objects.all().filter(wine__id=id, liked_it=True)
    return render(request, 'detail_wine.html', {'wines': wines, 'liked': liked})

def wineryDetail(request, id):
    wineries = Winery.objects.all().filter(id=id)
    return render(request, 'list_wineries.html', {'wineries': wineries})

## Edit Views

def editWine(request, id=None):
    # cellar = get_object_or_404(Cellar, id=id)

    try:
        wine = Wine.objects.get(id=id)
    except:
        wine = None

    # winery = Winery.objects.all()
    # WineFormSet = inlineformset_factory(Wine, Winery, )

    form = WineForm(request.POST or  None, request.FILES or None, instance=wine)
    # form = WineFormSet(request.POST or None, instance=wine,)
    if form.is_valid():
        # form = form.save(commit=False)
        # wine = Wine.objects.get(id=form.id)
        # print(wine)
        # print(request.FILES.get('image-clear'))
        # wine.image = request.FILES.get('image-clear')
        # wine.etiquette = request.FILES.get('etiquette-clear')
        form = form.save()
        if request.FILES.get('image'):
            image = request.FILES.get('image', None)
            form.image = image
            form.save()
        if request.FILES.get('etiquette'):
            etiquette = request.FILES.get('etiquette', None)
            form.etiquette = etiquette
            form.save()
        # form.save()
        return HttpResponseRedirect('/wine/wines/')
    return render(request, 'edit_wine.html', {'form': form})


def editWinery(request, id=None):
    # cellar = get_object_or_404(Cellar, id=id)

    try:
        winery = Winery.objects.get(id=id)
    except:
        winery = None

    # winery = Winery.objects.all()
    # WineFormSet = inlineformset_factory(Winery, Wine, fields=('winery', ))

    form = WineryForm(request.POST or None, instance=winery)
    # form = WineFormSet(request.POST or None, instance=winery,)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('/wine/wineries/')
    return render(request, 'edit_winery.html', {'form': form})
