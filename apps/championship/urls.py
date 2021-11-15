from django.urls import path
from .views import principalView, allChampionshipsView, reviewChampionship, newChampionship, get_fonts

urlpatterns = [
    path('',principalView,name='principalView'),
    path('championships',allChampionshipsView,name='championshipsView'),
    path('review/<int:cID>',reviewChampionship,name='reviewChampionship'),
    path('new_championship',newChampionship,name='newChampionship'),
    path('fonts',get_fonts,name='get_fonts')
]