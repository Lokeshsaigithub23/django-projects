from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse
def date_time_info(reqiest):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1>hello guest very'
    if h<12:
        msg+='good morning'
    elif h<16:
        msg+='good afternoon'
    elif h<21:
        msg+='good evening'
    else:
        msg+='good night'
    msg+='</h1><hr>'
    msg+='<h1>now the server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)            