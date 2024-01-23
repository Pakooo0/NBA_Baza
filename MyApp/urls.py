from xml.etree.ElementInclude import include

from django.urls import path

import MyApp
from MyApp import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('addplayer', views.addplayer, name="addplayer"),
    path('teams', views.teams, name="teams"),
    path('players', views.players, name="players"),
    path('coach', views.coach, name="coach"),
    path('hall', views.hall, name="hall"),
    path('stats', views.stats, name="stats"),
    path('match', views.match, name="match"),
    path('addteam', views.addteam, name="addteam"),
    path('home', views.home, name="home"),
    path('add_team', add_team, name='add_team'),
    path('add_player', add_player, name='add_player'),
    path('addcoach', views.addcoach, name='addcoach'),
    path('add_coach', add_coach, name='add_coach'),
    path('addhall',views.addhall, name="addhall"),
    path('add_hall',add_hall, name="add_hall"),
    path('addmatch', views.addmatch, name="addmatch"),
    path('add_match',add_match, name="add_match")
]
