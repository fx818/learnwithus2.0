from django.urls import path
from .views import *

urlpatterns = [
    path('practicecode/', programrunner, name="program-runner"),
]