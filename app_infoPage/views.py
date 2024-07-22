from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from .forms import contactForm

class aboutTemplate(TemplateView):
    template_name = 'app_infoPage/about.html'
    


def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('msg') 
    else:
        form = contactForm()
    return render(request,'app_infoPage/contact.html',{'forms':form})


class copyrightTemplate(TemplateView):
    template_name = 'app_infoPage/copyright.html'
class teamTemplate(TemplateView):
    template_name = 'app_infoPage/team.html'
class terms_and_conditionsTemplate(TemplateView):
    template_name = 'app_infoPage/terms_and_conditions.html'