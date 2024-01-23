from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django import forms


# Create your views here.
def index(request):
    return render(request, 'index.html')


def addplayer(request):
    teams = klub.objects.all()
    return render(request, 'addplayer.html', {'teams': teams})


@csrf_exempt
def teams(request):
    teams = klub.objects.all()
    response = []
    if request.method == 'POST':
        do_usuniecia = klub.objects.get(pk=request.POST['usun'])
        do_usuniecia.delete()
    for team in teams:
        response.append(
            {"team": team, "zawodnicy": zawodnicy.objects.filter(klub=team), "trener": trener.objects.filter(klub=team),
             "hala": hala.objects.filter(klub=team)})

    return render(request, 'teams.html', {'teams': response})


@csrf_exempt
def coach(request):
    coaches = trener.objects.all()
    if request.method == 'POST':
        do_usuniecia = trener.objects.get(pk=request.POST['usun'])
        do_usuniecia.delete()

    return render(request, 'coach.html', {'coaches': coaches})


@csrf_exempt
def players(request):
    players = zawodnicy.objects.all()
    if request.method == 'POST':
        do_usuniecia = zawodnicy.objects.get(pk=request.POST['usun'])
        do_usuniecia.delete()

    return render(request, 'players.html', {'players': players})


@csrf_exempt
def hall(request):
    halls = hala.objects.all()
    if request.method == 'POST':
        do_usuniecia = hala.objects.get(pk=request.POST['usun'])
        do_usuniecia.delete()

    return render(request, 'hall.html', {'halls': halls})


def stats(request):
    teams = klub.objects.all()

    return render(request, 'stats.html',{'teams':teams})


def addmatch(request):
    teams = klub.objects.all()
    return render(request, 'addmatch.html', {'teams': teams})


@csrf_exempt
def match(request):
    mecze = mecz.objects.all()
    if request.method == 'POST':
        do_usuniecia = mecz.objects.get(pk=request.POST['usun'])

        s1 = do_usuniecia.gospodarz.statystyki

        s1.punkty -= do_usuniecia.punkty_gosp
        s1.zbiorki -= do_usuniecia.zbiorki_gosp
        s1.bloki -= do_usuniecia.bloki_gosp
        s1.przechwyty -= do_usuniecia.przechwyty_gosp
        s1.wygrane -= do_usuniecia.wygrane_gosp
        s1.przegrane -= do_usuniecia.przegrane_gosp

        s1.save()
        s2 = do_usuniecia.gosc.statystyki

        s2.punkty -= do_usuniecia.punkty_gosc
        s2.zbiorki -= do_usuniecia.zbiorki_gosc
        s2.bloki -= do_usuniecia.bloki_gosc
        s2.przechwyty -= do_usuniecia.przechwyty_gosc
        s2.wygrane -= do_usuniecia.wygrane_gosc
        s2.przegrane -= do_usuniecia.przegrane_gosc

        s2.save()

        do_usuniecia.delete()

    return render(request, 'match.html', {'mecze': mecze})



def addteam(request):
    return render(request, 'addteam.html')


def home(request):
    return render(request, 'home.html')


def addcoach(request):
    teams = klub.objects.all()
    return render(request, 'addcoach.html', {'teams': teams})


def addhall(request):
    teams = klub.objects.all()
    return render(request, 'addhall.html', {'teams': teams})


def add_team(request):
    if request.method == 'POST':
        nazwa_druzyny = request.POST['nazwa_druzyny']
        miasto = request.POST['miasto']
        konferencja = request.POST['konferencja']

        s = statystyki.objects.create(
            punkty=0,
            zbiorki=0,
            bloki=0,
            przechwyty=0,
            wygrane=0,
            przegrane=0,
        )
        s.save()

        klub.objects.create(
            nazwa_druzyny=nazwa_druzyny,
            miasto=miasto,
            konferencja=konferencja,
            statystyki=statystyki.objects.get(pk=s.pk)
        )
        return redirect('teams')

    return render(request, 'add_team.html')


def add_player(request):
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
            klub=druzyna
        )
        return redirect('players')

    return render(request, 'addplayer.html', {'teams': teams})


def add_coach(request):
    if request.method == 'POST':
        imie = request.POST['imie']
        nazwisko = request.POST['nazwisko']
        data_urodzenia = request.POST['data_urodzenia']
        narodowosc = request.POST['narodowosc']
        staz_w_druzynie = request.POST['staz_w_druzynie']
        druzyna_id = request.POST['druzyna']

        druzyna = klub.objects.get(id_klub=druzyna_id)

        trener.objects.create(
            imie=imie,
            nazwisko=nazwisko,
            data_urodzenia=data_urodzenia,
            narodowosc=narodowosc,
            staz_w_druzynie=staz_w_druzynie,
            klub=druzyna
        )
        return redirect('coach')

    return render(request, 'addcoach.html', {'teams': teams})


def add_hall(request):
    if request.method == 'POST':
        nazwa_hali = request.POST['nazwa_hali']
        pojemnosc = request.POST['pojemnosc']
        miasto = request.POST['miasto']
        adres = request.POST['adres']
        druzyna_id = request.POST['druzyna']

        druzyna = klub.objects.get(id_klub=druzyna_id)

        hala.objects.create(
            nazwa_hali=nazwa_hali,
            pojemnosc=pojemnosc,
            miasto=miasto,
            adres=adres,
            klub=druzyna

        )
        return redirect('hall')

    return render(request, 'addhall.html', {'teams': teams})


def add_match(request):
    if request.method == 'POST':
        druz1 = request.POST['druzy1']
        druz2 = request.POST['druzy2']
        punkty1 = request.POST['punkty1']
        punkty2 = request.POST['punkty2']
        zbiorki1 = request.POST['zbiorki1']
        zbiorki2 = request.POST['zbiorki2']
        bloki1 = request.POST['bloki1']
        bloki2 = request.POST['bloki2']
        przechwyty1 = request.POST['przechwyty1']
        przechwyty2 = request.POST['przechwyty2']

        druzy1 = klub.objects.get(id_klub=druz1)
        druzy2 = klub.objects.get(id_klub=druz2)
        wynik = f"{punkty1}:{punkty2}"
        if punkty1 > punkty2:
            wygrane1 = 1
            wygrane2 = 0
            przegrane1 = 0
            przegrane2 = 1
        else:
            wygrane1 = 0
            wygrane2 = 1
            przegrane1 = 1
            przegrane2 = 0

        mecz.objects.create(
            gospodarz=druzy1,
            gosc=druzy2,
            wynik=wynik,
            punkty_gosp = punkty1,
            zbiorki_gosp = zbiorki1,
            bloki_gosp = bloki1,
            przechwyty_gosp=przechwyty1,
            wygrane_gosp=wygrane1,
            przegrane_gosp = przegrane1,
            punkty_gosc=punkty2,
            zbiorki_gosc=zbiorki2,
            bloki_gosc=bloki2,
            przechwyty_gosc=przechwyty2,
            wygrane_gosc=wygrane2,
            przegrane_gosc=przegrane2,
        )

        s1 = statystyki.objects.get(pk=druzy1.statystyki.pk)

        s1.punkty += int(punkty1)
        s1.zbiorki += int(zbiorki1)
        s1.bloki += int(bloki1)
        s1.przechwyty += int(przechwyty1)
        s1.wygrane += int(wygrane1)
        s1.przegrane += int(przegrane1)

        s1.save()
        s2 = statystyki.objects.get(pk=druzy2.statystyki.pk)

        s2.punkty += int(punkty2)
        s2.zbiorki += int(zbiorki2)
        s2.bloki += int(bloki2)
        s2.przechwyty += int(przechwyty2)
        s2.wygrane += int(wygrane2)
        s2.przegrane += int(przegrane2)

        s2.save()

        return redirect('match')

    return render(request, 'addmatch.html', {'teams': teams})
