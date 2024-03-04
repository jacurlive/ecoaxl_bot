from rest_framework import generics
from rest_framework.response import Response

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


class AccountByTelegramIdView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        telegram_id = self.kwargs.get('telegram_id')
        try:
            account = Account.objects.get(telegram_id=telegram_id)
            serializer = self.get_serializer(account)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)



# class AddressCreateView(generics.CreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializers
