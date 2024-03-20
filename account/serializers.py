from rest_framework import serializers
from .models import Rates, Account, Place, Audio


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'
