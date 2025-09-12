from django.shortcuts import render

# Create your views here.
import datetime
def info_view(request):
    time=datetime.datetime.now()
    name='django'
    prerequisite='python'
    my_dict={'time':time,'name':name,'prerequisite':prerequisite}
    return render(request,'testapp/result.html',my_dict)

