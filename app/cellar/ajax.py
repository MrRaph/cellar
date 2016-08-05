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
from django_ajax.decorators import ajax
# Create your views here.
from .models import Cellar, Zone, Cell, Bottle
from .forms import CellarForm, ZoneForm, CellForm, BottleForm

@ajax
@login_required
def get_bottle_likes(request, id):
    likes = Bottle.objects.filter(wine__id=id, liked_it=True).count()
    return likes

@ajax
@login_required
def did_user_liked_bottle(request, id):
    liked_it = Bottle.objects.filter(wine__id=id, user=request.user).values_list('liked_it')
    return liked_it

@ajax
@login_required
def switch_like(request, id):
    bottle = Bottle.objects.filter(wine__id=id, user=request.user)[0]

    if bottle.liked_it:
        bottle.liked_it = False
        bottle.save()
        return "disliked"
    elif not bottle.liked_it:
        bottle.liked_it = True
        bottle.save()
        return "liked"

    return "Error"
