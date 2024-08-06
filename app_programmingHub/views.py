from django.shortcuts import render
from .programRunner import returnOutput
from .models import *

# Create your views here.
def programrunner(request, pk):
    obj = programmingQuestionsModel.objects.get(questionID=int(pk))
    if request.method == 'POST':
        data = request.POST['usercode']
        outputs = returnOutput(data,obj.testcases.testID)
        return render(request, 'app_programmingHub/program.html', {"outputs": outputs, "code":data, "question":obj})
    return render(request, 'app_programmingHub/program.html', {"question":obj})    

def allquestion(request):
    obj = programmingQuestionsModel.objects.all()
    no_of_question = len(obj)
    return render(request, "app_programmingHub/allprograms.html", {"allquestions":obj, "noofquestions":no_of_question})
    
    
