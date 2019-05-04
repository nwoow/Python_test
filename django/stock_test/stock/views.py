from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    latest_question_list = "dddd"
    template = loader.get_template('stock/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))