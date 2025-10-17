from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')

from testapp.forms import AddItemsForm
def additems_view(request):
    form=AddItemsForm()
    response=render(request,'testapp/addiitem.html',{'form':form})
    if request.method=='POST':
        form=AddItemsForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['itemname']
            quantity=form.cleaned_data['quantity']
            response.set_cookies(name,quantity)
    return response

def display_items_view(request):
    return render(request,'testapp/displayitems.html')

