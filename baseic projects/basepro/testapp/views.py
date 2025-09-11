from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def frist_view(request):
    s='<h1>frist view</h1>'
    return HttpResponse(s)
def second_view(request):
    s='<h1>second view</h1>'
    return HttpResponse(s) 
def third_view(request):
    s='<h1>third view</h1>'
    return HttpResponse(s)
       