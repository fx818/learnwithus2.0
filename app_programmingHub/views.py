from django.shortcuts import render
from .programRunner import returnOutput

# Create your views here.
def programrunner(request):
    if request.method == 'POST':
        data = request.POST['usercode']
        # with open('utility/usercode.txt', 'w') as f:
        #     f.write(data)
        outputs = returnOutput(data)
        
        print("Successfully runned the code")
        
        print(outputs)
        
        return render(request, 'app_programmingHub/program.html', {"outputs": outputs, "code":data} )  
    # error = "Error bhai fir se check kr"
    return render(request, 'app_programmingHub/program.html')    
