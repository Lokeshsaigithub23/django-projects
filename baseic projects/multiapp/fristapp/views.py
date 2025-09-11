from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def wish1(request):
    s='<h1>hello this from frist app</h1>'
    return HttpResponse(s)