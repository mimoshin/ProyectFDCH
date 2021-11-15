from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from championship.models import ChampionshipInterface as CI
from .models import AthleteInterface as AI, fileslif
from competition.models import CompetitionFactory as CF


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
    if request.method == 'POST':
        data_dict = request.POST.dict()
        data_list = list(request.POST)
        id_comp, compts = [], []
        atleta = request.POST['athlete']

        for x in data_list:
            if 'COMPT' in x:
                cpk = x.split('-')[1]
                id_comp.append(cpk)
        
        for a in id_comp:
            compts.append(CF.get_competition(a))
        #for x in id_comp:
            #CF.new_inscription(atleta,x)

        print("atleta %s queriendo inscribirse a las pruebas:" %(atleta))
        for b in compts:
            print(b.pk)
            
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