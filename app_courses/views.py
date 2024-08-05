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

class PandasView(View):
    
    def get(self, request):
        details = PandasMCQModel.objects.all()
        serializer = PandasMCQSerializer(data=details, many = True)
        # print(serializer)
        if serializer.is_valid():
            return render(request, 'app_courses/pandas-quiz.html', {'data':serializer.data, "length":len(details)})
        return render(request, 'app_courses/pandas-quiz.html', {'data':serializer.data, "length":len(details)})
   
    
class MatplotlibView(View):
    
    def get(self, request):
        details = MatplotlibMCQModel.objects.all()
        serializer = MatplotlibMCQSerializer(data=details, many = True)
        # print(serializer)
        if serializer.is_valid():
            return render(request, 'app_courses/matplotlib-quiz.html', {'data':serializer.data, "length":len(details)})
        return render(request, 'app_courses/matplotlib-quiz.html', {'data':serializer.data, "length":len(details)})
    
class PythonQuizView(View):
    
    def get(self, request):
        details = PythonMCQModel.objects.all()
        serializer = PythonMCQSerializer(data=details, many = True)
        # print(serializer)
        if serializer.is_valid():
            return render(request, 'app_courses/python-quiz.html', {'data':serializer.data, "length":len(details)})
        return render(request, 'app_courses/python-quiz.html', {'data':serializer.data, "length":len(details)})
    
class CSSQuizView(View):
    
    def get(self, request):
        details = CSSMCQModel.objects.all()
        serializer = CSSMCQSerializer(data=details, many = True)
        # print(serializer)
        if serializer.is_valid():
            return render(request, 'app_courses/css-quiz.html', {'data':serializer.data, "length":len(details)})
        return render(request, 'app_courses/css-quiz.html', {'data':serializer.data, "length":len(details)})
    
class LinuxQuizView(View):
    
    def get(self, request):
        details = LinuxMCQModel.objects.all()
        serializer = LinuxMCQSerializer(data=details, many = True)
        # print(serializer)
        if serializer.is_valid():
            return render(request, 'app_courses/linux-quiz.html', {'data':serializer.data, "length":len(details)})
        return render(request, 'app_courses/linux-quiz.html', {'data':serializer.data, "length":len(details)})