from django.shortcuts import render
from django.views.generic import TemplateView

class notespediatemplate(TemplateView):
    def get(self, request):
        opportunities_for_fresher= ['Web Developer', 'App Developer' , 'Software Engineer', 'iOS Engineer', 'AI Developer', 'NLP Engineer', 'Data Scientist','Data Analyst', 'Data Engineer', 'Course Engineer']
        referance_books=['Sebesta, "Concept of Programming Language", Addison Wesley, 4th Edition, 2019',
                        ' Deitel & Deitel, “Internet and World Wide Web – How to Program”, Goldberg,Pearson Education. 3rd Edition 2003',
                        'Petersons, "Operating Systems", Addison Wesley, 9th Edition, 2012',
                        'Forouzan, B. A., Data Communications and Networking, McGraw-Hill Higher Education,3rd Edition, 2004.',
                        'A.S. Tannenbaum, “Computer Networks”, 3rd Edition, Prentice Hall India, 1997.']
        context= {
            'opportunities_for_fresher':opportunities_for_fresher,
            'referance_books':referance_books
        }
        return render(request,'app_notespedia/notespedia.html',context)



class CSEtemplate(TemplateView):
    template_name = 'app_notespedia/cse.html'

class ETtemplate(TemplateView):
    template_name = 'app_notespedia/et.html'

