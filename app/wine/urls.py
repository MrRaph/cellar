from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views

app_name = 'wine'
urlpatterns = [
    # List Views
    url(r'^wines/$', login_required(views.allWines), name='WineList'),
    url(r'^wineries/$', login_required(views.allWineries), name='WineriesList'),
    # Detail Views
    url(r'^wines/(?P<id>[0-9]+)$', login_required(views.wineDetail), name='WineDetail'),
    url(r'^wineries/(?P<id>[0-9]+)$', login_required(views.wineryDetail), name='WineryDetail'),
    # Add Views
    url(r'^wines/add/$', login_required(views.editWine), name='addWine'),
    url(r'^wineries/add/$', login_required(views.editWinery), name='addWinery'),
    # Edit Views
    url(r'^wines/edit/(?P<id>[0-9]+)/$', login_required(views.editWine), name='editWine'),
    url(r'^wineries/edit/(?P<id>[0-9]+)/$', login_required(views.editWinery), name='editWinery'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
