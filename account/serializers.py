from rest_framework import serializers
from .models import Rates, Account, Place, WorkerAccount, ClientOrder


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


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerAccount
        fields = "__all__"


class ClientOrderSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields = "__all__"
