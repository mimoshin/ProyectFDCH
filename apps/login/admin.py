from django.contrib import admin
from .models import AsociationAdmin,ClubAdmin,FedachiAdmin,ResultsAdmin,SuperAdmin,TrackAdmin

admin.site.register(AsociationAdmin)
admin.site.register(ClubAdmin)
admin.site.register(FedachiAdmin)
admin.site.register(ResultsAdmin)
admin.site.register(SuperAdmin)
admin.site.register(TrackAdmin)