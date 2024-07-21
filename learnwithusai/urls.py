from django.urls import path
from . import views

urlpatterns = [
    path('askalectogideon/', views.askalectogideon, name = 'askalectogideon'),
   
]