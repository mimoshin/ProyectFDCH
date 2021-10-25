from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal_view,name='champ_principal'),
    path('load_champs',views.load_championships,name='ld_champs'),
    path('delete_champs',views.delete_championship,name='del_champs'),
    path('load_stages',views.load_stages,name='ld_stages'),
    path('delete_stages',views.delete_stages,name='del_stages'),
    path('load_registrations',views.load_registrations,name='ld_regis'),
    path('delete_registrations',views.load_registrations,name='del_regis'),
]