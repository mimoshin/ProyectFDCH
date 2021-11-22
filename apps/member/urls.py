from django.urls import path
from .views import FedachiAdminAthletes, FedachiAdminChampionships, FedachiAdminClubs, FedachiAdminCompetitions, FedachiAdminEvents, FedachiAdminInscriptions, newClub, principalAdminsView

urlpatterns = [
    path('',principalAdminsView,name='principalAminsView'),
    path('usf_championships',FedachiAdminChampionships,name='fedachi_championships'),
    path('usf_competitions',FedachiAdminCompetitions,name='fedachi_competitions'),
    path('usf_inscriptions',FedachiAdminInscriptions,name='fedachi_inscriptions'),
    path('usf_athletes',FedachiAdminAthletes,name='fedachi_athletes'),
    path('usf_clubs',FedachiAdminClubs,name='fedachi_clubs'),
    path('usf_events',FedachiAdminEvents,name='fedachi_events'),
    #CHANGES
    path('new_club',newClub,name='create_club'),
]