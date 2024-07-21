from django.shortcuts import render
from .utils import results
from .models import userChatWithAI
import ast
# Create your views here.


def askalectogideon(request):
    username = request.user.username
    if request.method == 'POST':
        query = request.POST['query']
        # username = request.POST['username']
        output = results(query)
        output = output.split('\n')
        output = [x for x in output if x != 2]
        data = userChatWithAI.objects.create(user=username, query=query, response=output)
        data.save()
        all_data = userChatWithAI.objects.filter(user=username)
        all_data = all_data[::-1]
        str_list = all_data[0].response
        list_data = ast.literal_eval(str_list)
        data_output = []
        for i in all_data:
            data_output.append([i.query,ast.literal_eval(i.response)])
        if len(data_output) == 0:
            current = []
        else:
            current = data_output[0]
        return render(request, 'learnwithusai/askalectogideon.html', 
                      {'current_data': current})
    all_data = userChatWithAI.objects.filter(user=username)
    all_data = all_data[::-1]
    data_output = []
    for i in all_data:
        data_output.append([i.query,ast.literal_eval(i.response)])
    if len(data_output) == 0:
        current = []
    else:
        current = data_output[0]
    return render(request, 'learnwithusai/askalectogideon.html',
                  {'current_data': current,
                   })
