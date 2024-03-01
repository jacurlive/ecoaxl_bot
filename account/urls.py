from django.urls import path
from .views import RatesView, AccountCreateView, PlaceView

urlpatterns = [
    path('rates/', RatesView.as_view()),
    path('account/', AccountCreateView.as_view()),
    path("place/", PlaceView.as_view()),
    # path("address/", AddressCreateView.as_view())
]
