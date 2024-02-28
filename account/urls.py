from django.urls import path
from .views import RatesView, AccountCreateView

urlpatterns = [
    path('rates/', RatesView.as_view()),
    path('account/', AccountCreateView.as_view())
]
