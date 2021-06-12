from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def shopperView(request):
    return HttpResponse('Hello World')


def loginView(requset):
    return HttpResponse('Hello World')

def logoutView(requset):
    return HttpResponse('Hello World')

def shopcartView(requset):
    return HttpResponse('Hello World')