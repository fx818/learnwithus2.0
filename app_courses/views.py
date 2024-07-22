from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

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