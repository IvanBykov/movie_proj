from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.views.generic import ListView

# Create your views here.

from .models import Movie, Director, Actor


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        fals_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100,
        new_b_r=F('budget') + F('rating')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })

class ListShow(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors
    })

class ListActors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'



def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

def show_one_director(request, id_dir: int):
    director = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })

def show_one_actor(request, id_act: int):
    actor = get_object_or_404(Actor, id=id_act)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })
