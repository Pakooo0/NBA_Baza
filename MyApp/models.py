from django.db import models


# Create your models here.

class statystyki(models.Model):
    id_statystyki = models.AutoField(primary_key=True)
    punkty = models.IntegerField()
    zbiorki = models.IntegerField()
    bloki = models.IntegerField()
    przechwyty = models.IntegerField()
    wygrane = models.IntegerField()
    przegrane = models.IntegerField()

class klub(models.Model):
    id_klub = models.AutoField(primary_key=True)
    nazwa_druzyny = models.CharField(max_length=30)
    miasto = models.CharField(max_length=20)
    konferencja = models.CharField(max_length=15)
    statystyki = models.ForeignKey(statystyki, on_delete=models.CASCADE,default=0)




class trener(models.Model):
    id_trener = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.CharField(max_length=20)
    narodowosc = models.CharField(max_length=20)
    staz_w_druzynie = models.CharField(max_length=15)
    klub = models.ForeignKey(klub, on_delete=models.CASCADE,default=0)


class zawodnicy(models.Model):
    id_zawodnicy = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    narodowosc = models.CharField(max_length=20)
    wzrost = models.CharField(max_length=8)
    data_urodzenia = models.CharField()
    waga = models.CharField(max_length=8)
    klub = models.ForeignKey(klub, on_delete=models.CASCADE,default=0)






class mecz(models.Model):
    id_mecz = models.AutoField(primary_key=True)
    gosc = models.ForeignKey(klub, on_delete=models.CASCADE, default=0, related_name='mecze_gosc')
    gospodarz = models.ForeignKey(klub, on_delete=models.CASCADE, default=0, related_name='mecze_gospodarz')
    wynik = models.CharField(max_length=20)
    punkty_gosp = models.IntegerField(default=0)
    zbiorki_gosp = models.IntegerField(default=0)
    bloki_gosp = models.IntegerField(default=0)
    przechwyty_gosp = models.IntegerField(default=0)
    wygrane_gosp = models.IntegerField(default=0)
    przegrane_gosp = models.IntegerField(default=0)
    punkty_gosc = models.IntegerField(default=0)
    zbiorki_gosc = models.IntegerField(default=0)
    bloki_gosc = models.IntegerField(default=0)
    przechwyty_gosc = models.IntegerField(default=0)
    wygrane_gosc = models.IntegerField(default=0)
    przegrane_gosc = models.IntegerField(default=0)



class hala(models.Model):
    id_hala = models.AutoField(primary_key=True)
    nazwa_hali = models.CharField(max_length=30)
    pojemnosc = models.CharField(max_length=30)
    miasto = models.CharField(max_length=40)
    adres = models.CharField(max_length=40)
    klub = models.ForeignKey(klub, on_delete=models.CASCADE, default=0)
