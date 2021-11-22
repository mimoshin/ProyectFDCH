from django.urls import path
from .views import QFChampionship, newStage, principalView, allChampionshipsView, reviewChampionship, newChampionship

urlpatterns = [
    path('',principalView,name='principalView'),
    path('championships',allChampionshipsView,name='championshipsView'),
    path('review/<int:cID>',reviewChampionship,name='reviewChampionship'),
    path('new_championship',newChampionship,name='newChampionship'),
    #CHANGES
    path('new_stage/<int:champID>',newStage,name='create_stage'),
    #QUERYS
    path('QF_championship',QFChampionship,name="Query_Champ"),
]