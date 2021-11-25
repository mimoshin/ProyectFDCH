
import json
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import athleteInterface as AI, championshipInterface as CI, competitionInterface as CPI, testingInterface
from .models import testingInterface as TI
from championship.models import ChampionshipInterface as CHI
from competition.models import CompetitionFactory as CF,Competitions
from athlete.models import AthleteInterface as ATI
from member.models import MembersFactory as MF

#WEASYPRINT
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def generate_pdf(request):
    competition = Competitions.objects.get(id=2100)
    ctype = competition.get_type()
    heats = CF.get_heats(2100,ctype)
    data = {'competition':competition,'heats':heats}

    # Rendered
    html_string = render_to_string('grid2.html',data)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(result,content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    

    return response
################################################

#_____________principal views_____________________________
@login_required(login_url=('/'))
def principalView(request):
    return render(request,'testing/principalTesting.html',{'data':'data'})

@login_required(login_url=('/'))
def adminChampionships(request):
    all_champs = CHI.get_all_championships()
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
    return render(request,'testing/admChamps.html',{'champs':all_champs})

@login_required(login_url=('/'))
def adminCompetitions(request):
    all_champs = CF.get_all_competitions()
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
    return render(request,'testing/admCompetitions.html',{'champs':all_champs})

@login_required(login_url=('/'))
def adminInscriptions(request):
    all_champs = CHI.get_all_championships()
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
    return render(request,'testing/admInscriptions.html',{'champs':all_champs})

@login_required(login_url=('/'))
def adminAthletes(request):
    all_clubs = MF.get_all_clubs()
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
    return render(request,'testing/admAthletes.html',{'clubs':all_clubs})
#______________end principal views________________________

#_____________ QUERYS ____________________________________
@login_required(login_url=('/'))
def QTCompetitions(request):
    #Carga todas las competencias relacionadas a un torneo
    if request.method == 'GET':
        data = request.GET.dict()
        compts = TI.get_competitions(data['id'])
        return render(request,'nuevo.html',{'compts':compts})

@login_required(login_url=('/'))
def QTInscriptions(request):
    #Carga todas las inscripciones a una competencia
    if request.method == 'GET':
        data = request.GET.dict()
        insc = TI.get_inscriptions(data['id'])
        return render(request,'insc.html',{'inscriptions':insc})

@login_required(login_url=('/'))
def QTAthletes(request):
    #carga todos los atletas de un club
    if request.method == 'GET':
        data = request.GET.dict()
        insc = ATI.get_athletes_club(data['id'])
        return render(request,'athle.html',{'athletes':insc})
#_____________ END QUERYS ___________________________________

#_____________Changes _______________________________________
@login_required(login_url=('/'))
def NewInscriptions(request):
    if request.method == 'GET':
        data = request.GET.dict()
        response = CPI.generate_inscriptions(data['id'],data['num'])
        #insc = TI.get_inscriptions(data['id'])
        #return render(request,'insc.html',{'inscriptions':insc})
        return HttpResponse(response)

@login_required(login_url=('/'))
def RemoveInscriptions(request):
    if request.method == 'GET':
        data = request.GET.dict()
        print(data)
        response = CPI.remove_inscriptions(data)
        return HttpResponse(response)
#_____________end Changes ____________________________________


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


def detectFile(request):
    if request.method == 'POST':
        print(request.method)
        files = request.FILES
        if files:
            data = request.FILES['archivosubido']
            jFile = json.load(data)
            testingInterface.detectFile(data,jFile)
        else:
            print("aqui no ha pasado nada")
        return redirect('fedachi_championships')
        #return render(request,"testing/uploadFiles.html",{'data':'data'})
    return render(request,"testing/uploadFiles.html",{'data':'data'})