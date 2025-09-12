from django.shortcuts import render

# Create your views here.
import datetime, random
def request_view(request):
    msg_list=['the golden days ahead','Better to sleep more tim even in classroom','Tomorrow will be the best day of your life',
        'Tomorrow is the prefect day to propose ur GF','Very soon you will get job'      ]
    name_list=['loki','ani','anudeep','yesh']
    time=datetime.datetime.now()
    h=int(time.strftime('%H'))
    if h<=12:
        msg_list+='good morning'
    elif h<=16:
        msg_list+='good afternoon'
    elif h<=21:
        msg_list+='good evening'
    else:
        msg_list+='good night'
    name=random.choice(name_list)
    msg=random.choice(msg_list)
    return render(request,'testapp/astrology.html',)        
