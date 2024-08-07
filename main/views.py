import os

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View

from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Authorization')
        base_token_client = os.environ['TOKEN']
        base_token_worker = os.environ['WORKER-TOKEN']
        return token == base_token_client or token == base_token_worker


class MainView(View):

    def get(self, request):
        return render(request, 'main/index.html')


class ServeImageView(View):
    def get(self, request, filename):
        image_path = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        else:
            raise Http404("Image not found")
