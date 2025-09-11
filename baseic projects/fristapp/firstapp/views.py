from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def display(request):
    s = '<h1>Hello Students Welcome To Mahesh Sir Django Classes</h1>'
    return HttpResponse(s)