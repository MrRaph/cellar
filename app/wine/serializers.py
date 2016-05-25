from rest_framework import serializers

from .models import Wine, Winery


class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery


class WineSerializer(serializers.ModelSerializer):
    winery = WinerySerializer(read_only=True)

    class Meta:
        model = Wine
