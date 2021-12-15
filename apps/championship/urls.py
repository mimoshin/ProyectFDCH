from django.urls import path, re_path
from .views import QFChampionship, QFDisable, QFileEvt, modifyChampionship, newStage, principalView, allChampionshipsView, reviewChampionship, newChampionship

urlpatterns = [
    path('',principalView,name='principalView'),
    path('championships',allChampionshipsView,name='championshipsView'),
    path('review/<int:cID>',reviewChampionship,name='reviewChampionship'),
    path('new_championship',newChampionship,name='newChampionship'),
    #CHANGES
    path('new_stage/<int:champID>',newStage,name='create_stage'),
    path('modify_championship/<int:champID>',modifyChampionship,name='modifyChampionship'),
    #QUERYS
    path('QF_championship',QFChampionship,name="Query_Champ"),
    path('QF_disablestage',QFDisable,name="Query_DiableStage"),
    path('download_evt/<int:champID>',QFileEvt,name='download_evt'),
]