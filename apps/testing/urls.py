from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal_view,name='test_principal'),
    path('load_champs', views.load_championships,name='load_champs'),
    path('load_events',views.load_events,name='load_events'),
    path('load_competitions',views.load_competitions,name='load_competitions'),
    path('load_athletes',views.load_athletes,name='load_athletes'),
    path('delete_athletas',views.delete_athletes,name='delete_athletes'),
    path('load_stages',views.load_stages,name='load_stages'),
    path('generate_series',views.generate_series,name='gen_series'),
    path('delete_asn',views.delete_assignments,name='del_asn'),
]