from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def wish2(request):
    s='<h1>hello this from second app</h1>'
    return HttpResponse(s)
