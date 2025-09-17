from django.shortcuts import render

# Create your views here.
from testapp.models import employee
def emp_data_view(request):
    emp_list=employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/index.html',my_dict) 