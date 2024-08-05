from django.urls import path
from .views import MainView, ServeImageView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('media/<str:filename>', ServeImageView.as_view(), name='serve-image')
]
