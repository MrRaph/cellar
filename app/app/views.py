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
from wine.models import Wine, Store, Barcode, Address, Grape, Winery
from cellar.models import Cellar, Zone, Cell, Bottle

def index(request):
    if request.user.is_authenticated():
        cellars = Cellar.objects.all().filter(user=request.user)
        zones = Zone.objects.all().filter(cellar__user=request.user)
        cells = Cell.objects.all().filter(zone__cellar__user=request.user)

        return render(request, 'index.html', {'cellars': cellars, 'zones': zones, 'cells': cells})
    else:
        return render(request, 'index.html')
