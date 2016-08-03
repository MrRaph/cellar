from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views

app_name = 'cellar'
urlpatterns = [
    # List Views
    url(r'^cellars/$', login_required(views.myCellars), name='CellarList'),
    url(r'^zones/$', login_required(views.myZones), name='ZoneList'),
    url(r'^cells/$', login_required(views.myCells), name='CellList'),
    url(r'^bottles/$', login_required(views.myBottles), name='BottleList'),
    # Detail Views
    url(r'^cellars/(?P<id>[0-9]+)$', login_required(views.cellarDetail), name='CellarDetail'),
    url(r'^zones/(?P<id>[0-9]+)$', login_required(views.zoneDetail), name='ZoneDetail'),
    url(r'^cells/(?P<id>[0-9]+)$', login_required(views.cellDetail), name='CellDetail'),
    url(r'^bottles/(?P<id>[0-9]+)$', login_required(views.bottleDetail), name='BottleDetail'),
    # Add Views
    url(r'^cellars/add/$', login_required(views.editCellar), name='addCellar'),
    url(r'^zones/add/$', login_required(views.editZone), name='addZone'),
    url(r'^cells/add/$', login_required(views.editCell), name='addCell'),
    url(r'^bottles/add/$', login_required(views.editBottle), name='addCell'),
    # Edit Views
    url(r'^cellars/edit/(?P<id>[0-9]+)/$', login_required(views.editCellar), name='editCellar'),
    url(r'^zones/edit/(?P<id>[0-9]+)/$', login_required(views.editZone), name='editZone'),
    url(r'^cells/edit/(?P<id>[0-9]+)/$', login_required(views.editCell), name='editCell'),
    url(r'^bottles/edit/(?P<id>[0-9]+)/$', login_required(views.editBottle), name='editBottle'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
