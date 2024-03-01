from rest_framework import generics

from .models import Rates, Account, Place
from .serializers import RatesSerializer, AccountSerializer, PlaceSerializer


class RatesView(generics.ListAPIView):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer


class PlaceView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# class AddressCreateView(generics.CreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializers
