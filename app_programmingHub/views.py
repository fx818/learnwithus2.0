from django.shortcuts import render
from .programRunner import returnOutput
from .models import *

# Create your views here.
def programrunner(request, pk):
    obj = programmingQuestionsModel.objects.get(questionID=int(pk))
    if request.method == 'POST':
        user = request.user
        data = request.POST['usercode']
        outputs = returnOutput(data,obj.testcases.testID)
        if outputs[-1] == ['You have passed all the test cases']:
            submission = submissionModel.objects.create(submissionID = int(pk),submissionDetail=outputs,submittedBy=user, status="Solved",question=obj)
        else:
            submission = submissionModel.objects.create(submissionID = int(pk),submissionDetail=outputs,submittedBy=user, status="Attempted", question=obj)
        submission.save()
        return render(request, 'app_programmingHub/program.html', {"outputs": outputs, "code":data, "question":obj})
    return render(request, 'app_programmingHub/program.html', {"question":obj})    

def allquestion(request):
    obj = programmingQuestionsModel.objects.all()
    no_of_question = len(obj)
    return render(request, "app_programmingHub/allprograms.html", {"allquestions":obj, "noofquestions":no_of_question})
    
def seeAllSubmission(request, pk):
    user = request.user 
    if user.is_authenticated:
        submissionDetail = submissionModel.objects.filter(submissionID=int(pk), submittedBy=user)
    else:
        submissionDetail = None
    if len(submissionDetail)==0:
        submissionDetail = False
        return render(request, 'app_programmingHub/programSubmission.html', {"submissionDetail":""})

    return render(request, 'app_programmingHub/programSubmission.html', {"submissionDetail":submissionDetail[::-1]})
