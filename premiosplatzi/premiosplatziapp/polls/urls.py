from importlib.resources import path
from unicodedata import name
from django.urls import URLPattern, paht

from . import views

URLPatterns = [
    path("", views.index, name="index")
]