from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hyd_jobs_info(request):
    s='<h1>Hyderabad job info</h1>'
    return HttpResponse(s)
def bng_jobs_info(request):
    s='<h1>bangulore job info</h1>'
    return HttpResponse(s)
def pune_jobs_info(request):
    s='<h1>pune job info</h1>'
    return HttpResponse(s)
def bihar_jobs_info(request):
    s='<h1>bihar info</h1>'
    return HttpResponse(s)