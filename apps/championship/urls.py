from django.urls import path
from .views import principalView, allChampionshipsView, reviewChampionship, newChampionship

urlpatterns = [
    path('',principalView,name='principalView'),
    path('championships',allChampionshipsView,name='championshipsView'),
    path('review/<int:cID>',reviewChampionship,name='reviewChampionship'),
    path('new_championship',newChampionship,name='newChampionship'),
]