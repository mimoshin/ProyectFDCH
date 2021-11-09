from django.urls import path
from . import views

urlpatterns = [
    path('',views.stats_views,name='stats'),
    path('gene',views.generar_champs,name='generar_champs'),
    path('gene2',views.generar_etapas,name='generar_etapas'),
    path('gene3',views.generar_competencias,name='generar_competencias'),
    path('gene4',views.inscribir_enmasa,name='ins_masa'),
]