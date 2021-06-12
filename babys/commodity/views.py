from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def commodityView(request):
    return HttpResponse('Hello World')


def detailView(requset):
    return HttpResponse('Hello World')
