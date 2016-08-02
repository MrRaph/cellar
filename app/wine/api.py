from rest_framework import viewsets

from .serializers import WineSerializer
from .models import Wine


class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
