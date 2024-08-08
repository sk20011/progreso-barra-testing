# miapp/urls.py

from django.urls import path
from .views import my_view

urlpatterns = [
    path('progress/', my_view, name='progress'),
]
