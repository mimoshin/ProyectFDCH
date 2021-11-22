from django.urls import path
from .views import QFathletes, alternative, athletesInscription, fileslifV, newAthlete, veratleta
urlpatterns = [
    path('inscription/<int:cID>',athletesInscription,name='athletesInscription'),
    path('atleta/<int:AID>',veratleta,name='veratleta'),
    path('filescarga',fileslifV,name='verfile'),
    path('prueba',alternative,name='probandoinscripcion'),
    #QUERYS
    path('QF_athletes',QFathletes,name='Query_athletes'),
    #CHANGES
    path('new_athlete',newAthlete,name='create_athlete'),

]