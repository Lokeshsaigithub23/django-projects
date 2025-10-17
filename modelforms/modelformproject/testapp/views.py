from django.shortcuts import render

# Create your views here.
from testapp.forms import StudentForm
def student_view(request):
    form = StudentForm()
    return render(request,'testapp/studentform.html',{'form':form})

def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Record inserted into DB successfully.....')
    form = StudentForm()
    return render(request,'testapp/studentform.html',{'form':form})

