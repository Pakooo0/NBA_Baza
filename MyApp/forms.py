from django import forms
from .models import trener,klub,hala

class TrenerForm(forms.ModelForm):
    class Meta:
        model = trener
        fields = ['imie', 'nazwisko', 'data_urodzenia', 'narodowosc', 'staz_w_druzynie', 'klub']

    def __init__(self, *args, **kwargs):
        super(TrenerForm, self).__init__(*args, **kwargs)
        self.fields['klub'].queryset = klub.objects.all()

class HalaForm(forms.ModelForm):
    class Meta:
        model = hala
        fields = ['nazwa_hali', 'pojemnosc', 'miasto', 'kod_pocztowy', 'adres', 'klub']

    def __init__(self, *args, **kwargs):
        super(HalaForm, self).__init__(*args, **kwargs)
        self.fields['klub'].queryset = klub.objects.all()