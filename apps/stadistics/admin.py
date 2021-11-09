from django.contrib import admin
from .models import champ_stadistics, athletes_stadistics
# Register your models here.
admin.site.register(champ_stadistics)
admin.site.register(athletes_stadistics)