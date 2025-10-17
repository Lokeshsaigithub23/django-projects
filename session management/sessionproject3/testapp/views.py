from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def age_view(request):
    print(request.COOKIES)
    name = request.GET.get('name')
    response = render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def gf_view(request):
    print(request.COOKIES)
    name=request.COOKIES.get('name')
    age=request.GET.get('age')
    response=render(request,'testapp/gf.html',{'name':name})
    response.set_cookie('age',age)
    return response

def result_view(request):
    print(request.COOKIES)
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    gf=request.GET.get('gf')
    return render(request,'testapp/result.html',{'name':name,'age':age,'gf':gf})