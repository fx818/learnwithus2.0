from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import *
from .serializers import *

class CoursesTemplate(TemplateView):
    template_name = 'app_courses/courses.html'
class LinuxTemplate(TemplateView):
    template_name = 'app_courses/linux.html'
class PythonTemplate(TemplateView):
    template_name = 'app_courses/python-course.html'
class CTemplate(TemplateView):
    template_name = 'app_courses/C.html'
class cssTemplate(TemplateView):
    template_name = 'app_courses/css.html'
class HTMLTemplate(TemplateView):
    template_name = 'app_courses/html.html'
    

class numpyView(View):
    
    def get(self, request):
        details = NumpyMCQModel.objects.all()
        serializer = NumpyMCQSerializer(data=details, many = True)
        # print(serializer)
        if serializer.is_valid():
            return render(request, 'app_courses/numpy.html', {'data':serializer.data, "length":len(details)})
        return render(request, 'app_courses/numpy.html', {'data':serializer.data, "length":len(details)})