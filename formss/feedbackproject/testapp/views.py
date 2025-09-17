from django.shortcuts import render

# Create your views here.
from testapp.forms  import FeedBackForm
def feedback_view(request):
    submitted = False
    name = ''
    if request.method == 'POST':
        form=FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation sucess and printing feedback information')
            print('*'*55)
            print('name:',form.cleaned_data['name'])
            print('rollno:',form.cleaned_data['rollno'])
            print('emailid:',form.cleaned_data['email'])
            print('feedback:',form.cleaned_data['feedback'])
            submitted = True
            name=form.cleaned_data['name']
    form = FeedBackForm()
    return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'name':name})
         