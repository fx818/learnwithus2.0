from django.urls import path
from . import views

urlpatterns = [
    
    path("notespedia",views.notespediatemplate.as_view(),name='notespedia'),
    path("notespedia/cse",views.CSEtemplate.as_view(),name='cse'),
    path("notespedia/et",views.CSEtemplate.as_view(),name='et'),

]