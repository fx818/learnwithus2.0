from django.urls import path
from . import views

urlpatterns = [
    
    path('opportunities',views.opportunities,name = 'opportunities'),
    path("internshipupdatesatlearnwithus",views.internshipupdatesatlearnwithus,name='internshipupdatesatlearnwithus'),
    path("competetionupdatesatlearnwithus",views.competetionupdatesatlearnwithus,name='competetionupdatesatlearnwithus'),
    path("scholarshipupdatesatlearnwithus",views.scholarshipupdatesatlearnwithus,name='scholarshipupdatesatlearnwithus'),
    path("jobupdatesatlearnwithus",views.jobupdatesatlearnwithus,name='jobupdatesatlearnwithus'),
]