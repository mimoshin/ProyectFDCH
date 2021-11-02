from django.contrib import admin
from .models import (events,competitions,speedHeats,mdHeats,jumpHeats,throwHeats,
                     speedAssignments,mdAssignments,jumpAssignments,throwAssignments)

admin.site.register(events)
admin.site.register(competitions)
admin.site.register(speedHeats)
admin.site.register(mdHeats)
admin.site.register(jumpHeats)
admin.site.register(throwHeats)
admin.site.register(speedAssignments)
admin.site.register(mdAssignments)
admin.site.register(jumpAssignments)
admin.site.register(throwAssignments)