from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.aboutTemplate.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
    path('copyright/', views.copyrightTemplate.as_view(), name='copyright'),
    path('team/', views.teamTemplate.as_view(), name='team'),
    path('terms_and_conditions/', views.terms_and_conditionsTemplate.as_view(), name='terms_and_conditions'),
]