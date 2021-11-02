from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_excel,name='cargar_excel'),
    path('horario', views.cargar_horario,name='cargar_horario'),
    path('vercarga',views.mostrar_datos,name='mostrar_datos'),
]