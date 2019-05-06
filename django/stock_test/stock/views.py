from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Stock
from django_pandas.io import read_frame


def index(request):
    latest_question_list = Stock.objects.all()
    qs = Stock.objects.all()
    # df = qs.to_dataframe(fieldnames=['symbol', 'delayedprice', 'high'])
    df = "hh"
    template = loader.get_template('stock/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'df': df,
    }
    return HttpResponse(template.render(context, request))
def json(request):
    context = {
        'latest_question_list': "error",  
    }
    template = loader.get_template('stock/json.html')

    return HttpResponse(template.render(context, request))    
