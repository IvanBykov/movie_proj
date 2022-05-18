from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.ListShow.as_view()),
    path('director/<int:id_dir>', views.show_one_director, name='director-detail'),
    path('actors/', views.ListActors.as_view()),
    path('actors/<int:id_act>', views.show_one_actor, name='actor-detail'),
]
