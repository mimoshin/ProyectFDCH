from django.contrib import admin
from django.utils.timezone import activate

# Register your models here.
from .models import (championship, champ_log, category, champ_category, stage, stage_log, 
                     test, competition, inscription, track_series,
                     serie, track_inscription, second_track_inscription)
# Register your models here.

admin.site.register(championship)
admin.site.register(champ_log)
admin.site.register(category)
admin.site.register(champ_category)
admin.site.register(stage)
admin.site.register(stage_log)
admin.site.register(test)
admin.site.register(competition)
admin.site.register(inscription)
admin.site.register(track_series)
admin.site.register(serie)
admin.site.register(track_inscription)
admin.site.register(second_track_inscription)
