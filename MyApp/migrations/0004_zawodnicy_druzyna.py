# Generated by Django 5.0.1 on 2024-01-17 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_hala_klub_liga_nba_mecz_statystyki_trener_zawodnicy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zawodnicy',
            name='druzyna',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyApp.klub'),
        ),
    ]
