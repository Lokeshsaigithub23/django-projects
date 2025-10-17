from django.shortcuts import render

# Create your views here.
from testapp.models import FilterModel
def data_view(request):
    records=FilterModel.objects.all()
    return render(request,'testapp/data.html',{'records':records})
    