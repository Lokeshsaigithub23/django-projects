from django.shortcuts import render

# Create your views here.

import datetime
from django.http import HttpResponse
def time_info(request):
    date=datetime.datetime.now()
    msg='<h1> good evening <h1/><hr>'
    msg+='<h2>now server time is:' +str(date)+ '</h2>'
    return HttpResponse(msg)
