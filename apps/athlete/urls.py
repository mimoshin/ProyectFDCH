from django.urls import path
from .views import QFathletes, alternative, athletesInscription, deleteAthlete, fileslifV, modifyAthlete, newAthlete, veratleta
urlpatterns = [
    path('inscription/<int:cID>',athletesInscription,name='athletesInscription'),
    path('atleta/<int:AID>',veratleta,name='veratleta'),
    path('filescarga',fileslifV,name='verfile'),
    path('insc_athlete/<int:champ>',alternative,name='athlete_inscription'),
    #QUERYS
    path('QF_athletes',QFathletes,name='Query_athletes'),
    #CHANGES
    path('new_athlete',newAthlete,name='create_athlete'),
    path('del_athlete',deleteAthlete,name='delete_athlete'),
    path('modi_athlete/<int:athleID>',modifyAthlete,name='modify_athlete'),

]