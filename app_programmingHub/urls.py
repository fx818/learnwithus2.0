from django.urls import path
from .views import *

urlpatterns = [
    path('practicecode/', allquestion, name="allquestions"),
    path('practicecode/<int:pk>/', programrunner, name="program-runner"),
]