from rest_framework import generics

from .models import Rates, Account
from .serializers import RatesSerializer, AccountSerializer


class RatesView(generics.ListAPIView):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
