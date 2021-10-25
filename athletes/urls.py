from os import name
from athletes.utils import repair_rut
from django.urls import path
from . import views

urlpatterns =[
    path('',views.principal_view,name='atle_principal'),
    path('repair_names',views.repair_names,name='repair_names'),
    path('repair_ruts',views.repair_ruts,name='repair_ruts'),
    path('load',views.load_athletes,name="ld_athletes"),
    path('viewA',views.view_athletes,name="view_A"),
    path('delete_atl',views.delete_athletes,name='del_athletes')
]