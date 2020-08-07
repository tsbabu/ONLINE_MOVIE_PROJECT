from django.http import HttpResponse
from django.shortcuts import render, redirect
from ONLINE_MOVIES.settings import ONLINE_MOVIES_FILE
import json
from .models import Movies



def addmovie(request):
    dict_data = json.loads(open(ONLINE_MOVIES_FILE).read())
    movies = [x for x in dict_data['d']]
    return render(request, "addmovie.html", {"data": movies})


def save_data(request):
    name=request.GET.get('name')
    movie_type=request.GET.get('type')
    rank=request.GET.get('rank')
    casting=request.GET.get('casting')
    year=request.GET.get('year')
    Movies(movie_name=name,type=movie_type,rank=rank,casting=casting,release_date=year).save()
    return redirect("addmovie")


def search_movie(request):
    return render(request,'search_movie.html')


def search(request):
    name=request.POST.get('t1')
    res=Movies.objects.get(movie_name=name)
    return render(request,'search_movie.html',{'data':res})