from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.index,name='index'),
    path('addplayer', views.addplayer,name="addplayer"),
    path('teams', views.teams, name="teams"),
    path('players', views.players, name="players"),
    path('coach', views.coach, name="coach"),
    path('hall', views.hall, name="hall"),
    path('stats', views.stats, name="stats"),
    path('match', views.match, name="match"),
    path('table', views.table, name="table"),
    path('addteam', views.addteam, name="addteam"),
    path('home', views.home, name="home"),
]