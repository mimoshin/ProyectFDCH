import json
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from base.const import EVENT_TYPE_CHOICES
from base.utils import Qlog_user
from athlete.models import AthleteInterface as AI
from championship.models import ChampionshipFactory as CF
from competition.models import CompetitionFactory as CPF
from login.models import UserFactory as UF
from testing.models import testingInterface as TI
from .models import MembersFactory as MF

#_____________ FILTER VIEWS _______________________________
def principalAthletesView(request):
    if Qlog_user(request.user):
        template = 'Internal/members/allAthletes.html'
    else: 
        template = 'External/members/allAthletes.html'
    athletes = []
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        data = request.GET.dict()
        athletes = AI.get_athletes_filter(data)
        if not athletes:
            athletes = 'EMPTY'
    return render(request,template,{'athletes':athletes})

@login_required(login_url=('/'))
def principalAdminsView(request):
    options = {'Fedachi':FedachiAV}
    user = UF.get_type_user(request.user)
    if user[0]:
        return options[user[1]](request)
    else:
        #Usuario anonimo
        return redirect('principalView')

@login_required(login_url=('/'))
def FedachiAV(request):
    return render(request,'members/FedachiUser/principal.html',{'data':'Fedachi Admin View'})
#_____________ END FILTER VIEWS ___________________________

#_____________ FEDACHI VIEWS _______________________________
@login_required(login_url=('/'))
def FedachiAdminChampionships(request):
    #Administracion de campeonatos USER: FEDACHI
    all_champs = CF.get_all_championships().order_by('-startDate')
    dataT = {'data':'F.Championship.A.V','champs':all_champs}
    if request.method == 'POST':
        files = request.FILES
        if files:
            data = request.FILES['archivosubido']
            jFile = json.load(data)
            TI.detectFile(data,jFile)
            return redirect('fedachi_championships')
    template = 'members/FedachiUser/championships/adminChampionships.html'
    return render(request,template,dataT)


@login_required(login_url=('/'))
def FedachiAdminCompetitions(request):
    #Administracion de competencias USER: FEDACHI
    all_champs = CF.get_all_championships
    if request.method == 'POST':
        files = request.FILES
        if files:
            data = request.FILES['archivosubido']
            jFile = json.load(data)
            TI.detectFile(data,jFile)
            if data._name == 'sports.json':
                return redirect('fedachi_events')
            return redirect('fedachi_competitions')
    return render(request,'members/FedachiUser/competitions/adminCompetitions.html',{'champs':all_champs})

@login_required(login_url=('/'))
def FedachiAdminInscriptions(request):
    all_champs = CF.get_all_championships()
    #Administracion de inscripciones USER: FEDACHI
    return render(request,'members/FedachiUser/competitions/adminInscriptions.html',{'champs':all_champs})

@login_required(login_url=('/'))
def FedachiAdminAthletes(request):
    #Administracion de atletas USER: FEDACHI
    all_clubs = MF.get_all_clubs()
    dataT = {'data':'F.Athletes.A.V','clubs':all_clubs}
    template = 'members/FedachiUser/athletes/adminAthletes.html'
    if request.method == 'POST':
        files = request.FILES
        if files:
            data = request.FILES['archivosubido']
            jFile = json.load(data)
            TI.detectFile(data,jFile)
            return redirect('fedachi_athletes')
    return render(request,template,dataT)

@login_required(login_url=('/'))
def FedachiAdminClubs(request):
    #Administracion de clubes USER: FEDACHI
    all_clubs = MF.get_all_clubs()
    dataT = {'data':'F.Clubs.A.V','clubs':all_clubs}
    template = 'members/FedachiUser/members/adminClubs.html'
    if request.method == 'POST':
        files = request.FILES
        if files:
            data = request.FILES['archivosubido']
            jFile = json.load(data)
            TI.detectFile(data,jFile)
            return redirect('fedachi_clubs')
    return render(request,template,dataT)

@login_required(login_url=('/'))
def FedachiAdminEvents(request):
    #Administracion de eventos USER: FEDACHI
    all_events = CPF.get_all_events()
    dataT = {'data':'F.Events.A.V','events':all_events,'types':EVENT_TYPE_CHOICES}
    template = 'members/FedachiUser/competitions/adminEvents.html'
    if request.method == 'POST':
        files = request.FILES
        if files:
            data = request.FILES['archivosubido']
            jFile = json.load(data)
            TI.detectFile(data,jFile)
            return redirect('fedachi_events')
    return render(request,template,dataT)
#_____________ END FEDACHI VIEWS ___________________________

#_____________ OTHER VIEWS _______________________________
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
def newClub(request):
    if request.method == 'POST':
        data = request.POST.dict()
        MF.new_club(data)
        return redirect('fedachi_clubs')

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