from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def list_movies_view(request):
    movie_list=movie.objects.all()
    return render (request,'testapp/listmovies.html',{'movie_list':movie_list})

def add_movie_view(request):
    form = MovieForm()
    return render(request,'testapp/addmovie.html',{'form':form})

def add_movie_view(request):
    form=MovieForm()    
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_view(request) 
    return render(request,'testapp/addmovie.html',{'form':form})