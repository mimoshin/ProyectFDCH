from competition.utils import renderPDF
from django.shortcuts import redirect, render
from .models import athleteInterface as AI, championshipInterface as CI, competitionInterface as CPI
from championship.models import ChampionshipInterface as CHI

#_____________principal views_____________________________
def principalView(request):
    return render(request,'testing/principalTesting.html',{'data':'data'})

def adminChampionships(request):
    all_champs = CHI.get_all_championships()
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
    return render(request,'testing/admChamps.html',{'champs':all_champs})


#______________end principal views

def loadChampionships(request):
    CI.load_championships()
    return redirect('testPrincipal')

def deleteChampionships(request):
    CI.delete_championships()
    return redirect('testPrincipal')

def loadEvents(request):
    CPI.load_events()
    return redirect('testPrincipal')

def deleteEvents(request):
    CPI.delete_events()
    return redirect('testPrincipal')

def loadCompetitions(request):
    CPI.load_competitions()
    return redirect('testPrincipal')

def deleteCompetitions(request):
    CPI.delete_competition()
    return redirect('testPrincipal')

def loadAthletes(request):
    AI.load_athletes()
    return redirect('testPrincipal')

def deleteAthletes(request):
    AI.delete_athletes()
    return redirect('testPrincipal')

def loadStages(request):
    CI.load_stages()
    return redirect('testPrincipal')

def deleteStages(request):
    CI.delete_stages()
    return redirect('testPrincipal')

def loadClubs(request):
    CI.load_clubs()
    return redirect('testPrincipal')

def deleteClubs(request):
    CI.delete_clubs()
    return redirect('testPrincipal')

def generate_series(request):
    CPI.generate_series()
    return redirect('testPrincipal')

def delete_assignments(request):
    CPI.delete_assignments()
    return redirect('testPrincipal')

def loadJumpHeats(request):
    CPI.load_jumpHeats()
    return redirect('testPrincipal')

def deleteJumpHeats(request):
    CPI.delete_jumpHeats()
    return redirect('testPrincipal')

def loadJumps(request):
    CPI.load_jumps()
    return redirect('testPrincipal')

def deleteJumps(request):
    CPI.delete_jumps()
    return redirect('testPrincipal')

def loadJumpParticipation(request):
    CPI.load_jump_participations()
    return redirect('testPrincipal')

def deleteJumpParticipation(request):
    CPI.delete_jump_participations()
    return redirect('testPrincipal')

def loadHJumpHeats(request):
    CPI.load_HjumpHeats()
    return redirect('testPrincipal')

def loadHJumps(request):
    CPI.load_Hjumps()
    return redirect('testPrincipal')

def loadThrowHeats(request):
    CPI.load_throwheats()
    return redirect('testPrincipal')

def deleteThrowHeats(request):
    CPI.delete_throwheats()
    return redirect('testPrincipal')

def loadThrows(request):
    CPI.load_throws()
    return redirect('testPrincipal')

def deleteThrows(request):
    CPI.delete_throws()
    return redirect('testPrincipal')

def loadParticipationThrows(request):
    CPI.load_throw_participations()
    return redirect('testPrincipal')

def deleteParticipationThrows(request):
    CPI.delete_throws_participations()
    return redirect('testPrincipal')