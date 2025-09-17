from django.shortcuts import render

# Create your views here.
from testapp.forms import studentForm
def student_input_view(request):
    submitted=False
    sname=''
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            print('Form validation success and print data')
            print('rollno:',form.cleaned_data['rollno'])
            print('name:',form.cleaned_data['name'])
            print('marks:',form.cleaned_data['marks'])  
            sname=form.cleaned_data['name']
            submitted = True
    form = studentForm()        
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted,'sname':sname})

