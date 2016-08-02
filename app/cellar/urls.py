from django.conf.urls import patterns, include, url
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
    # Detail Views
    url(r'^cellars/(?P<id>[0-9]+)$', login_required(views.cellarDetail), name='CellarDetail'),
    url(r'^zones/(?P<id>[0-9]+)$', login_required(views.zoneDetail), name='ZoneDetail'),
    url(r'^cells/(?P<id>[0-9]+)$', login_required(views.cellDetail), name='CellDetail'),
    # Edit Views
    url(r'^cellars/edit/(?P<id>[0-9]+)/$', login_required(views.editCellar), name='editCellar'),
    url(r'^zones/edit/(?P<id>[0-9]+)/$', login_required(views.editZone), name='editZone'),
    url(r'^cells/edit/(?P<id>[0-9]+)/$', login_required(views.editCell), name='editCell'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
