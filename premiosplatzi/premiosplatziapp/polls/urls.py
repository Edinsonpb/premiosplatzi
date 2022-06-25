from importlib.resources import path
from unicodedata import name
from django.urls import URLPattern, paht

from . import views

urlpatterns = [
    path("", views.index, name="index")
]