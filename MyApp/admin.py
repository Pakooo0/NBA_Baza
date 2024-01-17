from django.contrib import admin
from .models import liga_nba
from .models import zawodnicy
from .models import klub
from .models import hala
from .models import statystyki
from .models import trener
from .models import mecz


admin.site.register(zawodnicy)
admin.site.register(klub)
admin.site.register(liga_nba)
admin.site.register(hala)
admin.site.register(statystyki)
admin.site.register(trener)
admin.site.register(mecz)
