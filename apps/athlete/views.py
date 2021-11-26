import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from base.utils import json_to_list
from championship.models import ChampionshipInterface as CI
from .models import AthleteInterface as AI, fileslif
from competition.models import CompetitionFactory as CF
from member.models import MembersFactory as MF


#-----------------FILTER VIEWS ----------------------------
#----------------------------------------------------------
#-----------------INTERNAL VIEWS --------------------------
@login_required(login_url='/')
def athletesInscription(request,cID):
    champ = CI.get_championship(cID)
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        dataGET = request.GET.dict()
        if dataGET:
            athletes = AI.get_athletes(dataGET)
            return render(request,'Internal/athlete/inscription.html',{'champ':champ,'athletes':athletes})
    return render(request,'Internal/athlete/inscription.html',{'champ':champ})



def alternative(request):
    #Hacer Seguimiento a la inscripcion
    if request.method == 'POST':
        data_dict = request.POST.dict()
        data_list = list(request.POST)
        id_comp, compts = [], []
        try:
            atleta = request.POST['athlete']
            print("datalist",data_list)
            for x in data_list:
                if 'COMPT' in x:
                    cpk = x.split('|')[1]
                    id_comp.append(cpk)
            for a in id_comp:
                compts.append(CF.get_competition(a))
            for x in id_comp:
                CF.new_inscription(atleta,x)

            print("atleta %s queriendo inscribirse a las pruebas:" %(atleta))
            for b in compts:
                print(b.pk)
        except Exception as e:
            print("error al inscribir atleta",e)
            
        #return redirect('/atletas/inscripcion/33?name=&category=1')
    return redirect('principalView')
#----------------------------------------------------------


#-----------------EXTERNAL VIEWS --------------------------
def veratleta(request,AID):
    athle = AI.get_athlete(AID)
    return render(request,'testing/atleta.html',{'atleta':athle})

def fileslifV(request):
    if request.method == 'GET':
        #fileslif.objects.create(archivo='',texto='')
        print(request.GET)
    todo = fileslif.objects.all()
    return render(request,'texto.html',{'total':todo})
#----------------------------------------------------------


#_____________ QUERYS ____________________________________
def QFathletes(request):
    #Obtener listado de atletas
    if request.method == 'GET':
        data = request.GET.dict()
        athletes_list = AI.get_athletes_club(data['id'])
        dataT = {'athletes':athletes_list}
        template = 'members/FedachiUser/athletes/athletesList.html'
        return render(request,template,dataT)
#_____________ END QUERYS ________________________________

#_____________ CHANGES ____________________________________
@login_required(login_url='/')
def newAthlete(request):
    if request.method == 'POST':
        data = request.POST.dict()
        AI.new_athlete(data)
        return redirect('fedachi_athletes')

@login_required(login_url='/')
def modifyAthlete(request,athleID):
   
    if request.method == 'POST':
        data = request.POST.dict()
        AI.modify_athlete(athleID,data)
        return redirect('fedachi_athletes')
    if request.method == 'GET':
        athlete = AI.get_athlete(athleID)
        allclubs = MF.get_all_clubs()
        return render(request,'Internal/athlete/athleModify.html',{'athlete':athlete,'clubs':allclubs})

@login_required(login_url='/')
def deleteAthlete(request):
    if request.method == 'GET':
        data = request.GET.dict()
        athlete = AI.delete_athlete(data['id'])
        return HttpResponse(True)
#_____________ END QUERYS ____________________________________