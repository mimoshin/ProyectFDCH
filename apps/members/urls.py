from django.urls import path
from . import views

urlpatterns = [
    path('',views.athletes_view,name='athletes'),
    path('inscripcion/<int:c_id>',views.athletes_inscription,name='athletes_inscription'),
    path('Q',views.Question,name='question'),
    path('data',views.load_data,name='load_data'),
    path('ins',views.inscription,name='inscription'),
    path('prueba',views.alternative,name='probando'),
]