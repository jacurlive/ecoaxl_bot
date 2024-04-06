from django.urls import path
from .views import RatesView, AccountCreateView, PlaceView, AccountByTelegramIdView, AudioListView, AccountDeleteAPIView, WorkerCreateView, WorkerAccountByTelegramIdView, ClientOrderCreateView

urlpatterns = [
    path("rates/", RatesView.as_view()),
    path("account/", AccountCreateView.as_view()),
    path("place/", PlaceView.as_view()),
    path("account/<int:telegram_id>", AccountByTelegramIdView.as_view()),
    path("account/delete/<int:telegram_id>", AccountDeleteAPIView.as_view()),
    path("worker/", WorkerCreateView.as_view()),
    path("worker/<int:telegram_id>", WorkerAccountByTelegramIdView.as_view()),
    path("order/create/", ClientOrderCreateView.as_view()),
    path("audio/", AudioListView.as_view())
]
