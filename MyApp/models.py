from django.db import models


# Create your models here.


class liga_nba(models.Model):
    id_liga = models.AutoField(primary_key=True)
    ilosc_zespolow = models.CharField(max_length=10)
    kraj = models.CharField(max_length=20)
    puchar = models.CharField(max_length=15)
    sezon = models.CharField(max_length=8)


class klub(models.Model):
    id_klub = models.AutoField(primary_key=True)
    nazwa_druzyny = models.CharField(max_length=30)
    miasto = models.CharField(max_length=20)
    konferencja = models.CharField(max_length=15)



class trener(models.Model):
    id_trener = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.CharField(max_length=20)
    narodowosc = models.CharField(max_length=15)
    staz_w_druzynie = models.CharField(max_length=15)
    klub = models.ForeignKey(klub, on_delete=models.CASCADE,default=0)


class zawodnicy(models.Model):
    id_zawodnicy = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=10)
    nazwisko = models.CharField(max_length=20)
    narodowosc = models.CharField(max_length=15)
    wzrost = models.CharField(max_length=8)
    data_urodzenia = models.CharField()
    waga = models.CharField(max_length=8)
    klub = models.ForeignKey(klub, on_delete=models.CASCADE,default=0)


class statystyki(models.Model):
    id_statystyki = models.CharField(max_length=30)
    punkty = models.AutoField(primary_key=True)
    zbiorki = models.CharField(max_length=10)
    bloki = models.CharField(max_length=20)
    przechwyty = models.CharField(max_length=15)
    wygrane = models.CharField(max_length=8)
    przegrane = models.CharField(max_length=20)


class mecz(models.Model):
    id_mecz = models.AutoField(primary_key=True)
    id_gosc = models.CharField(max_length=30)
    id_gospodarz = models.CharField(max_length=20)
    wynik = models.CharField(max_length=10)
    lokalizacja = models.CharField(max_length=15)


class hala(models.Model):
    id_hala = models.AutoField(primary_key=True)
    nazwa_hali = models.CharField(max_length=30)
    pojemnosc = models.CharField(max_length=30)
    miasto = models.CharField(max_length=10)
    kod_pocztowy = models.CharField(max_length=15)
    adres = models.CharField(max_length=40)
    klub = models.ForeignKey(klub, on_delete=models.CASCADE, default=0)
