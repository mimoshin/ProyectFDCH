from django.contrib import admin
from .models import (Competitions, Events, Inscriptions, SpeedHeats, SpeedAssignments, MidHeats, MidAssignments, 
                    JumpHeats, JumpAssignments, ThrowHeats, ThrowAssignments, JumpParticipation,ThrowParticipation)

admin.site.register(Competitions)
admin.site.register(Events)
admin.site.register(Inscriptions)
admin.site.register(SpeedHeats)
admin.site.register(SpeedAssignments)
admin.site.register(MidHeats)
admin.site.register(MidAssignments)
admin.site.register(JumpHeats)
admin.site.register(JumpAssignments)
admin.site.register(ThrowHeats)
admin.site.register(ThrowAssignments)
admin.site.register(JumpParticipation)
admin.site.register(ThrowParticipation)