from django.urls import path
from django.utils.dateparse import parse_date
from . import views

urlpatterns = [
    path('',views.athletes_view,name='athletes'),
    path('inscripcion/<int:c_id>',views.athletes_inscription,name='athletes_inscription'),
    path('Q',views.Question,name='question'),
    path('data',views.load_data,name='load_data'),
    path('ins',views.inscription,name='inscription'),
    path('prueba',views.alternative,name='probando'),
    path('delete_all',views.delete_all,name='delete_all'),
    #pruebas
    path('query1', views.query_compt, name='query_compt'),
]