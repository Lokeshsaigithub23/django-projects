from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def wish(request):
    return render(request,'testapp/wish.html')

import datetime
def wish(request):
    date=datetime.datetime.now()
    my_dict={'insert_date':date}
    return render(request,'testapp/wish.html',content=my_dict)

def wish(request):
    date=datetime.datetime.now()
    name='lokesh'
    marks=89
    rollno=101
    my_dict={'insert_date':date,'name':name,'marks':marks,'rollno':rollno}
    return render(request,'testapp/wish.html',my_dict)