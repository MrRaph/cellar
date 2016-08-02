from rest_framework import serializers

from .models import Cellar, Zone, Cell
from wine.serializers import WineSerializer


class CellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellar

class ZoneSerializer(serializers.ModelSerializer):
    cellar = CellarSerializer(read_only=True)

    class Meta:
        model = Zone

class CellSerializer(serializers.ModelSerializer):
    wine = WineSerializer(read_only=True)
    zone = ZoneSerializer(read_only=True)

    # class Meta:
    model = Cell

    def get_object(self):
        return Cellar.objects.all().filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
