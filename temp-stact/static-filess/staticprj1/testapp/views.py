from django.shortcuts import render

# Create your views here.
def results_view(request):
    subjects = {'s1':'Python','s2':'Django','s3':'REST_API','s4':'Numpy,Pandas,Matplotlib'}
    return render(request,'testapp/index.html',subjects)