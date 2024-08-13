from . import views
from django.urls import path

urlpatterns = [
    path('courses/', views.CoursesTemplate.as_view(), name='courses'),
    path('courses/linux/',views.LinuxTemplate.as_view(), name = 'linux'),
    path('courses/python-tutorial/',views.PythonTemplate.as_view(), name = 'python'),
    path('courses/C/',views.CTemplate.as_view(), name = 'C'),
    path('courses/HTML/',views.HTMLTemplate.as_view(),name = 'HTML'),
    path('courses/css/',views.cssTemplate.as_view(), name = 'css'),
    # path('courses/numpy/',views.numpyView.as_view(), name = 'numpy-quiz'),
    # path('courses/pandas/',views.PandasView.as_view(), name = 'pandas-quiz'),
    # path('courses/matplotlib/',views.MatplotlibView.as_view(), name = 'matplotlib-quiz'),
    # path('courses/python-tutorial/python-quiz/',views.PythonQuizView.as_view(), name = 'python-quiz'),
    # path('courses/python-tutorial/python-quiz/<str:topictag>',views.PythonQuizView.as_view(), name = 'python-quiz'),
    # path('courses/css/css-quiz/',views.CSSQuizView.as_view(), name = 'css-quiz'),
    # path('courses/linux/linux-quiz/',views.LinuxQuizView.as_view(), name = 'Linux-quiz'),
]