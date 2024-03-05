from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies


# Create your views here.

def index(request):
    movie = Movies.objects.all()
    context = {'movie_list' : movie}
    return render(request,'index.html', context)


def detail(request, movie_id):
    x = Movies.objects.get(id=movie_id)
    return render(request, "detail.html", {'y':x})
