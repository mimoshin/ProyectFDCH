from os import name
from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('',views.init_view,name='init_test'),
    path('form',views.form_test,name='form_test'),
    path('inscriptions',views.inscription_test,name='ins_test'),
    path('load_data',views.load_menu,name='load_menu'),
    path('load_athletes',views.load_athletes,name='load_athletes'),
    path('load_clubs',views.load_clubs,name='load_clubs'),
    path('load_champs',views.load_championships,name='load_champs')
]