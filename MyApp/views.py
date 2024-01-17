from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import klub, zawodnicy, trener
from .forms import TrenerForm, HalaForm

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
def addcoach(request):
    return render(request, 'addcoach.html')
def addhall(request):
    return render(request, 'addhall.html')

def add_team(request):
    if request.method == 'POST':
        nazwa_druzyny = request.POST['nazwa_druzyny']
        miasto = request.POST['miasto']
        konferencja = request.POST['konferencja']

        klub.objects.create(
            nazwa_druzyny=nazwa_druzyny,
            miasto=miasto,
            konferencja=konferencja
        )
        return redirect('teams')
    teams = klub.objects.all()
    return render(request, 'add_team.html')


def add_player(request):
    teams = klub.objects.all()

    if request.method == 'POST':
        imie = request.POST['imie']
        nazwisko = request.POST['nazwisko']
        narodowosc = request.POST['narodowosc']
        wzrost = request.POST['wzrost']
        data_urodzenia = request.POST['data_urodzenia']
        waga = request.POST['waga']
        druzyna_id = request.POST['druzyna']

        druzyna = klub.objects.get(id_klub=druzyna_id)

        zawodnicy.objects.create(
            imie=imie,
            nazwisko=nazwisko,
            narodowosc=narodowosc,
            wzrost=wzrost,
            data_urodzenia=data_urodzenia,
            waga=waga,
            druzyna=druzyna
        )
        return redirect('teams')

    return render(request, 'add_player.html', {'teams': teams})

def add_coach(request):
    kluby = klub.objects.all()  # Pobieranie wszystkich klubów z bazy danych
    if request.method == 'POST':
        form = TrenerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Przekierowanie po dodaniu trenera
    else:
        form = TrenerForm()

    return render(request, 'addcoach.html', {'form': form, 'kluby': kluby})


def add_hall(request):
    kluby = klub.objects.all()  # Pobieranie wszystkich klubów z bazy danych
    if request.method == 'POST':
        form = HalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Przekierowanie po dodaniu hali
    else:
        form = HalaForm()

    return render(request, 'addhall.html', {'form': form, 'kluby': kluby})