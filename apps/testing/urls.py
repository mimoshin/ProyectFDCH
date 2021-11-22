from django.urls import path
from .views import*

urlpatterns = [
    path('',principalView,name='testPrincipal'),
    #admin
    path('admin_champs',adminChampionships,name='adminChamps'),
    path('admin_competitions',adminCompetitions,name='adminCompts'),
    path('admin_inscriptions',adminInscriptions,name='adminInsc'),
    path('admin_athletes',adminAthletes,name='adminAthles'),
    #load data
    path('load_champs', loadChampionships,name='loadChamps'),
    path('delete_champs', deleteChampionships,name='deleteChamps'),
    path('load_events',loadEvents,name='loadEvents'),
    path('delete_events',deleteEvents,name='deleteEvents'),
    path('load_competitions',loadCompetitions,name='loadCompetitions'),
    path('delete_competitions',deleteCompetitions,name='deleteCompetitions'),
    path('load_athletes',loadAthletes,name='loadAthletes'),
    path('delete_athletas',deleteAthletes,name='deleteAthletes'),
    path('load_stages',loadStages,name='loadStages'),
    path('delete_stages',deleteStages,name='deleteStages'),
    path('load_clubs',loadClubs,name='loadClubs'),
    path('delete_clubs',deleteClubs,name='deleteClubs'),
    path('generate_series',generate_series,name='gen_series'),
    path('delete_asn',delete_assignments,name='del_asn'),
    path('load_jheats',loadJumpHeats,name='loadJumpHeats'),
    path('delete_jheats',deleteJumpHeats,name='deleteJumpHeats'),
    path('load_hjumpheats',loadHJumpHeats,name='loadHJumpHeats'),
    path('load_hjumps',loadHJumps,name='loadHJumps'),
    path('load_jumps',loadJumps,name='loadJumps'),
    path('delete_jumps',deleteJumps,name='deleteJumps'),
    path('load_theats',loadThrowHeats,name='loadThrowHeats'),
    path('delete_theats',deleteThrowHeats,name='deleteThrowHeats'),
    path('load_throws',loadThrows,name='loadThrows'),
    path('delete_throws',deleteThrows,name='deleteThrows'),
    path('load_throwsPA',loadParticipationThrows,name='loadThrowsPA'),
    path('delete_throwsPA',deleteParticipationThrows,name='deleteThrowsPA'),
    path('load_jpaticipation',loadJumpParticipation,name='loadJumpParticipation'),
    path('delete_jparticipation',deleteJumpParticipation,name='deleteJumpParticipation'),
    #QUERYS
    path('Q_competitions',QTCompetitions,name='Q_competitions'),
    path('Q_inscriptions',QTInscriptions,name='Q_inscriptions'),
    path('Q_athletes',QTAthletes,name='Q_athletes'),
    #CHANGES
    path('New_inscriptions',NewInscriptions,name='New_inscriptions'),
    path('remove_inscriptions',RemoveInscriptions,name='remove_inscriptions'),
    #DETECT
    path('detectandofile',detectFile,name='detectFiles'),
    
]