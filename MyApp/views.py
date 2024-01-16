from django.shortcuts import render
from django.http import HttpResponse
from .models import NBAT, NBAP


# Create your views here.
def index(request):
    return render(request, 'index.html')


def addplayer(request):
    return render(request, 'addplayer.html')


def teams(request):
    T1 = NBAT()
    T1.id = 0
    T1.name = 'Chicago Bulls'

    T2 = NBAT()
    T2.id = 0
    T2.name = 'Los Angeles Lakers'

    NBATs = [T1, T2]
    return render(request, 'teams.html', {'TMS': NBATs})

def player(request):
    P1 = NBAP()
    P1.id = 0
    P1.name = 'DeMar DeRozan'
    P1.club = 'Chicago Bulls'

    P2 = NBAP()
    P2.id = 1
    P2.name = 'LeBron James'
    P2.club = 'Los Angeles Lakers'

    NBAPs = [P1,P2]
    return render(request, 'players.html',{'PLR': NBAPs})

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
