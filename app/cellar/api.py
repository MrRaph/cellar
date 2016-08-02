from rest_framework import viewsets, permissions, generics, authentication, filters
from rest_framework.decorators import detail_route

from .serializers import CellarSerializer, ZoneSerializer, CellSerializer
from .models import Cellar, Zone, Cell

# def get_current_user():
#     return request.user


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    filter_backends = (                                                     
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class CellarViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Cellar.objects.all()
    serializer_class = CellarSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
