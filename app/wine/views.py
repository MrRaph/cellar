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
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Wine, Store, Barcode, Address, Grape, Winery
from .forms import WineForm, StoreForm, BarcodeForm, AddressForm, AddressForm, GrapeForm, WineryForm

from cellar.models import Bottle

## List Views

@login_required
def allWines(request):
    wines = Wine.objects.all()
    return render(request, 'list_wines.html', {'wines': wines})

@login_required
def allWineries(request):
    wineries = Winery.objects.all()
    return render(request, 'list_wineries.html', {'wineries': wineries})

## Detail Views

@login_required
def wineDetail(request, id):
    wines = Wine.objects.all().filter(id=id)
    # wineries = Winery.objects.all().filter()
    liked = Bottle.objects.all().filter(wine__id=id, liked_it=True)
    return render(request, 'detail_wine.html', {'wines': wines, 'liked': liked})

@login_required
def wineryDetail(request, id):
    wineries = Winery.objects.all().filter(id=id)
    return render(request, 'list_wineries.html', {'wineries': wineries})

## Edit Views

@login_required
def editWine(request, id=None):
    try:
        wine = Wine.objects.get(id=id)
    except:
        wine = None

    form = WineForm(request.POST or  None, request.FILES or None, instance=wine)
    if form.is_valid():
        form = form.save()
        if request.FILES.get('image'):
            image = request.FILES.get('image', None)
            form.image = image
            form.save()
        if request.FILES.get('etiquette'):
            etiquette = request.FILES.get('etiquette', None)
            form.etiquette = etiquette
            form.save()
        return HttpResponseRedirect('/wine/wines/')
    return render(request, 'edit_wine.html', {'form': form})

@login_required
def editWinery(request, id=None):
    try:
        winery = Winery.objects.get(id=id)
        try:
            address = Address.objects.all().filter(id=winery.address.id)[0]
        except:
            address = None
    except:
        winery = None
        address = None

    address_form = AddressForm(request.POST or None, instance=address)
    form = WineryForm(request.POST or None, instance=winery)
    
    if address_form.is_valid():
        address = address_form.save(commit=False)
        address.save()
    if form.is_valid():
        form = form.save(commit=False)
        form.address = address
        form.save()
        return HttpResponseRedirect('/wine/wineries/')
    return render(request, 'edit_winery.html', {'form': form, 'address_form': address_form})
