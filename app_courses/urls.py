from . import views
from django.urls import path

urlpatterns = [
    path('courses/', views.CoursesTemplate.as_view(), name='courses'),
    path('courses/linux',views.LinuxTemplate.as_view(), name = 'linux'),
    path('courses/python',views.PythonTemplate.as_view(), name = 'python'),
    path('courses/C',views.CTemplate.as_view(), name = 'C'),
    path('courses/HTML',views.HTMLTemplate.as_view(),name = 'HTML'),
    path('courses/css',views.cssTemplate.as_view(), name = 'css'),
    path('courses/numpy',views.numpyView.as_view(), name = 'numpy'),
]