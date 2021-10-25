from django.contrib import admin
from .models import competition,sport,track_head2s,track2s,resume_track,resume_Hjump,resume_jump,resume_throw
# Register your models here.
admin.site.register(competition)
admin.site.register(sport)
admin.site.register(track_head2s)
admin.site.register(track2s)
admin.site.register(resume_track)
admin.site.register(resume_Hjump)
admin.site.register(resume_jump)
admin.site.register(resume_throw)