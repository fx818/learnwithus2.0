from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .forms import internshupUpdateForm, competetionUpdateForm, scholarshipUpdateForm, jobUpdateForm
from .models import jobModel, InternshipModel, CompetetionModel, scholarshipModel

@login_required
def internshipupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = internshupUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'app_opportunities/internshipupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'app_opportunities/internshipupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = internshupUpdateForm()
    return render(request,'app_opportunities/internshipupdates.html',{'forms':form})
    



@login_required
def competetionupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = competetionUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'app_opportunities/competetionupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'app_opportunities/competetionupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = competetionUpdateForm()
    return render(request,'app_opportunities/competetionupdates.html',{'forms':form})
    





@login_required
def scholarshipupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = scholarshipUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'app_opportunities/scholarshipupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'app_opportunities/scholarshipupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = scholarshipUpdateForm()
    return render(request,'app_opportunities/scholarshipupdates.html',{'forms':form})
    



@login_required
def jobupdatesatlearnwithus(request):
    user = request.user
    print(user.is_superuser)
    if request.method == 'POST':
        form = jobUpdateForm(request.POST, request.FILES)  # Add request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return render(
                request,
                'app_opportunities/jobupdates.html',
                {'msg':'Updated succesfully',
                 'forms':form
                }
            )
        else:
            return render(request,
                          'app_opportunities/jobupdates.html',
                          {'msg':'Form is not valid',
                           'forms':form
                           }
                        )
    else:
        form = jobUpdateForm()
    return render(request,'app_opportunities/jobupdates.html',{'forms':form})
    




def opportunities(request):
    internships = InternshipModel.objects.all()
    competetion = CompetetionModel.objects.all()
    scholarship = scholarshipModel.objects.all()
    job = jobModel.objects.all()
    
    print(internships)
    
    return render(request,'app_opportunities/opportunities.html',
                  {'internships':internships[::-1],
                   'competetions':competetion[::-1],
                   'scholarships':scholarship[::-1],
                   'jobs':job[::-1]
                   }
                  )