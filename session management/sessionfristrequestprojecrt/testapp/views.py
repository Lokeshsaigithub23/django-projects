from django.shortcuts import render

# Create your views here.
from testapp.forms import loginForm
def home_view(request):
    form=loginForm()
    return render(request,'testapp/home.html',{'form':form}) 

def datetime_view(request):
    name=request.GET['name']
    response=render(request,'testapp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response

import datetime
def result_view(request):
    name=request.COOKIES.get('name')
    date=datetime.datetime.now()
    return render(request,'testapp/result.html',{'name':name,'date':date})

