from django.urls import path
from .views import alternative, athletesInscription, fileslifV, veratleta
urlpatterns = [
    path('inscription/<int:cID>',athletesInscription,name='athletesInscription'),
    path('atleta/<int:AID>',veratleta,name='veratleta'),
    path('filescarga',fileslifV,name='verfile'),
    path('prueba',alternative,name='probandoinscripcion'),
]