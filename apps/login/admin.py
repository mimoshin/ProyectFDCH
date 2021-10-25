from django.contrib import admin
from .models import superAdmin,fedachiAdmin,asociationAdmin,clubAdmin,trackAdmin,resultsAdmin,judge

# Register your models here.
admin.site.register(superAdmin)
admin.site.register(fedachiAdmin)
admin.site.register(asociationAdmin)
admin.site.register(clubAdmin)
admin.site.register(trackAdmin)
admin.site.register(resultsAdmin)
admin.site.register(judge)