from django.contrib import admin
from .models import Super_admin, Fed_admin, Asociation_admin, Club_admin
# Register your models here.
admin.site.register(Super_admin)
admin.site.register(Fed_admin)
admin.site.register(Asociation_admin)
admin.site.register(Club_admin)