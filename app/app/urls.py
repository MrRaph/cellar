"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from wine.api import WineViewSet
from cellar.api import CellarViewSet, ZoneViewSet, CellViewSet

router = DefaultRouter()
router.register(r'wine', WineViewSet)
router.register(r'cellar', CellarViewSet)
router.register(r'zone', ZoneViewSet)
router.register(r'cell', CellViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('registration.backends.simple.urls')),
    # url(r'^api/', include(router.urls)),
    # url(r'^api/token/', obtain_auth_token, name='api-token'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

admin.site.site_header = _("Cellar")
admin.site.site_title = _("Cellar")
admin.site.index_title = _("Manage Your Wine")
admin.site.site_url = None
