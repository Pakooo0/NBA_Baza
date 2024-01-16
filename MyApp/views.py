from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def addplayer(request):
    return render(request, 'addplayer.html')
def teams(request):
    return render(request, 'teams.html')
def players(request):
    return render(request, 'players.html')
def coach(request):
    return render(request, 'coach.html')
def hall(request):
    return render(request, 'hall.html')
def stats(request):
    return render(request, 'stats.html')
def match(request):
    return render(request, 'match.html')
def table(request):
    return render(request, 'table.html')
def addteam(request):
    return render(request, 'addteam.html')
def home(request):
    return render(request, 'home.html')
