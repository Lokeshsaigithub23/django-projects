from django.shortcuts import render

# Create your views here.
from testapp.models import student
def student_view(request):
    student_list=student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'testapp/std.html',my_dict)

def student_view(request):
    student_list=student.objects.filter(marks__lt=35)
    student_list=student.objects.filter(marks__lte=35)
    student_list=student.objects.filter(marks__startswith='s')
    student_list=student.objects.all().order_by('marks')
    student_list=student.objects.all().order_by('marks') 