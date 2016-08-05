from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views, ajax

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
    # Delete Views
    url(r'^cellars/delete/(?P<id>[0-9]+)/$', login_required(views.cellarDelete), name='cellarDelete'),
    url(r'^zones/delete/(?P<id>[0-9]+)/$', login_required(views.zoneDelete), name='zoneDelete'),
    url(r'^cells/delete/(?P<id>[0-9]+)/$', login_required(views.cellDelete), name='cellDelete'),
    url(r'^bottles/delete/(?P<id>[0-9]+)/$', login_required(views.bottleDelete), name='bottleDelete'),

    ### AJAX ###
    url(r'^bottles/ajax/likes/(?P<id>[0-9]+)/$', login_required(ajax.get_bottle_likes), name='get_bottle_likes'),
    url(r'^bottles/ajax/liked_it/(?P<id>[0-9]+)/$', login_required(ajax.did_user_liked_bottle), name='did_user_liked_bottle'),
    url(r'^bottles/ajax/switch_like/(?P<id>[0-9]+)/$', login_required(ajax.switch_like), name='switch_like'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
