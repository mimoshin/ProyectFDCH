
from django.contrib.auth.decorators import login_required
from django.http import response
from django.http.response import HttpResponse,FileResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, View
from base.utils import Qlog_user
from base.const import FEDACHI_LOGO
from athlete.models import Athletes
from championship.models import ChampionshipFactory as CHF
from .models import CompetitionFactory as CF,SpeedAssignments
from .utils import renderPDF


#-----------------FILTER & GENERAL VIEWS ------------------
def startlistView(request,comptID):
    if Qlog_user(request.user):
        return internalSV(request,comptID)
    else:
        return externalSV(request,comptID)

def resultsView(request,comptID):
    if Qlog_user(request.user):
        return internalRV(request,comptID)
    else:
        return externalRV(request,comptID)

#----------------------------------------------------------

#-------------------INTERNAL VIEWS-------------------------
@login_required(login_url=('/'))
def competitionView(request,cID):
    templates = {1:'iCompetitionSP.html',2:'iCompetitionMD.html',3:'iCompetitionJP.html',4:'iCompetitionPV.html',5:'iCompetitionTW.html'}
    competition = CF.get_competition(cID)
    ctype = competition.get_type()
    insclist = CF.get_inscriptions(cID)
    heats = CF.get_heats(cID,ctype)
    return render(request,'Internal/competitions/'+templates[ctype],{'competition':competition,'heats':heats,'inscriptions':insclist})


@login_required(login_url=('/'))
def internalSV(request,comptID):
    templates = {1:'Internal/competitions/iStartlistSP.html',2:'Internal/competitions/iStartlistMD.html',
                3:'Internal/competitions/iStartlistJP.html',4:'Internal/competitions/iStartlistPV.html',5:'Internal/competitions/iStartlistTW.html'}
    if request.method == 'POST':
        data = request.POST.dict()
        print("recibiendo data",data)
    elif request.method == 'GET':
        pass
    competition = CF.get_competition(comptID)
    cID = competition.get_CID()
    ctype = competition.get_type()
    heats = CF.get_heats(comptID,ctype)

    return render(request,templates[ctype],{'cID':cID,'id':comptID,'competition':competition,'heats_data':heats})

@login_required(login_url='/')
def internalRV(request,comptID):
    #admin_view
    templates = {1:'Internal/competitions/iResultsSP.html',2:'Internal/competitions/iResultsMD.html',
                3:'Internal/competitions/iResultsJPV2.html',4:'Internal/competitions/iResultsPV.html',5:'Internal/competitions/iResultsTW.html'}
    #Obtengo la competencia
    competition = CF.get_competition(comptID)
    #obtengo el id del campeonato
    cID = competition.get_CID()
    #obtengo el tipo de competencia
    ctype = competition.get_type()
    
    #Obtengo la serie y sus atletas asignados
    heats = CF.get_heats(comptID,ctype)
    if request.method == 'POST':
        data = request.POST.dict()
        CF.changeResult(ctype,data['atleta'],data['value'])
        print("Cambiar resultado del atleta ",data['atleta'],"en la competencia id:" ,comptID)
        return HttpResponse('hola, ??funcion???')
    return render(request,templates[ctype],{'cID':cID,'id':comptID,'competition':competition,'heats_data':heats,'cpi':comptID})


@login_required(login_url=('/'))
def newCompetition(request,stID):
    if request.method == 'POST':
        data = request.POST.dict()
        response = CF.new_competition(stID,data)
        return HttpResponse(response)
    elif request.method == 'GET':
        pass

@login_required(login_url='/')
def Qcompetitions(request):
    if request.method == 'POST':
        dataPOST = request.POST.dict()
        print(dataPOST)
    elif request.method == 'GET':
        dataGET = request.GET.dict()
        if dataGET['obj'] == 'load_compt':
            print("consultando para cargar pruebas",dataGET)
            data = CF.get_compt_for_atle(dataGET)
        return HttpResponse(data)

@login_required
def genSeries(request,cID):
    if request.method == 'GET':
        data = request.GET.dict()
        CF.generate_series(cID,data)
        return HttpResponse(False)
    print("generar series")
    CF.generate_series(cID)
    return redirect('competition',cID)
#----------------------------------------------------------


#-------------------EXTERNAL VIEWS-------------------------
def externalSV(request,comptID):
    #client_view
    templates = {1:'External/competitions/eStartlistSP.html',2:'External/competitions/eStartlistMD.html',
                3:'External/competitions/eStartlistJP.html',4:'External/competitions/eStartlistPV.html',5:'External/competitions/eStartlistTW.html'}
    
    competition = CF.get_competition(comptID)
    cID = competition.get_CID()
    ctype = competition.get_type()
    heats = CF.get_heats(comptID,ctype)
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,templates[ctype],{'cID':cID,'id':comptID,'competition':competition,'heats_data':heats})

def externalRV(request,comptID):
    #client_view
    templates = {1:'External/competitions/eResultsSP.html',2:'External/competitions/eResultsMD.html',
                3:'External/competitions/eResultsJPV2.html',4:'External/competitions/eResultsPV.html',5:'External/competitions/eResultsTW.html'}
    competition = CF.get_competition(comptID)
    cID = competition.get_CID()
    ctype = competition.get_type()
    heats = CF.get_heats(comptID,ctype)
    return render(request,templates[ctype],{'cID':cID,'id':comptID,'competition':competition,'heats_data':heats})
#----------------------------------------------------------



def saltoV2(request,cp_id):
    competition = CF.get_competition(cp_id)
    cID = competition.get_CID()
    ctype = competition.get_type()
    heats = CF.get_heats(cp_id,ctype)
    return render(request,'External/competitions/eResultsJPV2.html',{'cID':cID,'id':cp_id,'competition':competition,'heats_data':heats})

def lanzV2(request,cp_id):
    competition = CF.get_competition(cp_id)
    cID = competition.get_CID()
    ctype = competition.get_type()
    heats = CF.get_heats(cp_id,ctype)
    return render(request,'External/competitions/eResultsTWV2.html',{'cID':cID,'id':cp_id,'competition':competition,'heats_data':heats})


def change_result(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print("quiero cambiar el resultado",data)
        return HttpResponse(False)
    if request.method == 'GET':
        return HttpResponse('hola')

def download_file(request):
    #Funcion de prueba de descarga de archivos
    filename ='hola.txt'
    excel = 'FORMATO TIPO PLANILLA LANZAMIENTOS (1).xlsx'
    response = FileResponse(open('static\\files\\'+excel,'rb'))
    return response

def download_startlist(request,Type):
    print("quiero descargar starlist",Type)
    #Retorna el archivo para su descarga
    #Implementar: Generacion de archivo con las series y el nombre de la prueba
    competition = CF.get_competition(Type)
    print(competition)
    excel = competition.file()
    response = FileResponse(open('static\\files\\'+excel,'wb+'))
    return response

def template(request):
    renderPDF('competitions/startlist.html','hola')
    return redirect('principal')

class startView(ListView):
    model = SpeedAssignments
    template_name = 'competitions/descargar.html'
    context_object_name = 'series'

class otroview(View):
    def get(self,request,*args,**kwargs):
        templates = {1:'competition/lista.html'}
        competition = CF.get_competition(1)
        heats = CF.get_heats(1,1)
        data = {'competition':competition,'heats':heats,'url':FEDACHI_LOGO}
        pdf = renderPDF(templates[1],data)
        return HttpResponse(pdf,content_type='application/pdf')


def pdfView(request,c_id):
    templates = {1:'competition/docs/speedST.html',2:'competition/docs/mdST.html',
                 3:'competition/docs/jumpST.html',4:'competition/docs/hjumpST.html',5:'competition/docs/throwST.html',}
               #3:'competition/docs/jumpST.html'
    if request.method == 'GET':
        competition = CF.get_competition(c_id)
        print(templates[competition.get_type()])
        ctype = competition.get_type()
        heats = CF.get_heats(c_id,ctype)
        data = {'competition':competition,'heats':heats,'url':FEDACHI_LOGO}
        pdf = renderPDF(templates[competition.get_type()],data)
        return HttpResponse(pdf,content_type='application/pdf')

def probandoGET(request):
    if request.method == 'POST':
        print("solicitando algo en post")
        return HttpResponse('aqui estoy consultando como cargar archivos')
    elif request.method == 'GET':
        print("solicitando algo en get")
    return render(request,'nuevo.html')

def verAtleta(request,id):
    athle = Athletes.objects.get(id=id)
    comps = CF.get_athlete_results(athle)
    return render(request,'External/atleta.html',{'atleta':athle,'competitions':comps})

def nuevoatleta(request):
    if request.method == 'POST':
        print("ingresar atleta",request.POST)
    return render(request,'External/nuevo.html',{'atleta':'data'})

#_____________ QUERYS ____________________________________
@login_required(login_url=('/'))
def newInsc(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print("consultando para cargar pruebas",data)
        compts = CF.get_compt_for_atle(data)
    return render(request,'Internal/athlete/inscriptionOptions.html',{'data':compts,'athle':data['atle'],'champ':data['champ']})
        


@login_required(login_url=('/'))
def QLCompetitions(request):
    #Carga todas las competencias relacionadas a un torneo
    if request.method == 'GET':
        data = request.GET.dict()
        compts = CF.get_competitions_champ(data['id'])
        return render(request,'members/FedachiUser/competitions/compInscription.html',{'compts':compts})

def Qjumps(request,asID):
    if request.method == 'POST':
        print("consultando saltos del atleta en la serie : ",asID)
        return JsonResponse(CF.get_jumps(asID),safe=False)
    elif request.method == 'GET':
        print("METODO GET LLAMADO, REVISAR Qjumps")
    return redirect('principalView')

def QFcompetitions(request):
    if request.method == 'GET':
        data = request.GET.dict()
        if data['option'] == 'all':
            competitions_list = CF.get_competitions_champ(data['id'])
            dataT = {'competitions':competitions_list}
            template = 'members/FedachiUser/competitions/competitionsList.html'
        elif data['option'] == 'dataC':
            competition = CF.get_competition(data['id'])
            print(competition)
            dataT = {'competition':competition}
            template = 'members/FedachiUser/competitions/competitionsData.html'
        return render(request,template,dataT)

def QFnewCompetition(request):
    if request.method == 'GET':
        data = request.GET.dict()
        template = 'members/FedachiUser/competitions/newCompetitionForm.html'
        events = CF.get_all_events()
        champ = CHF.get_championship(data['id'])
        stages = champ.stages_set.all()
        dataT = {'idC':data['id'],'events':events,'champ':champ,'stages':stages}
       
        return render(request,template,dataT)

def QFparticipations(request):
    template = {'1':'Internal/competitions/jumpParticipations.html',
                '2':'Internal/competitions/participations.html'}
    if request.method == 'GET':
        data  = request.GET.dict()
        participations = CF.get_my_participations(data['id'],data['type'])
        return render(request,template[data['type']],{'participations':participations,'id':data['id']})


@login_required(login_url=('/'))
def QInscriptions(request):
    if request.method == 'GET':
        dataGET = request.GET.dict()
        if dataGET['obj'] == 'load_compt':
            data = CF.get_compt_for_atle(dataGET)
        return render(request,'Internal/athlete/inscriptionOptions.html',{'data':data,'athle':dataGET['atle']})    
    
    if request.method == 'POST':
        data = request.POST.dict()
        compts = CF.get_compt_for_atle(data)
        return render(request,'Internal/athlete/inscriptionOptions.html',{'data':compts,'athle':data['atle'],'champ':data['champ']})
#__________________________________

#_____________ CHANGES ____________________________________
@login_required(login_url=('/'))
def newEvent(request):
    if request.method == 'POST':
        data = request.POST.dict()
        CF.new_event(data)
        return redirect('fedachi_events')

def insertParticipation(request):
    if request.method == 'GET':
        data  = request.GET.dict()
        pResponse = CF.set_participations(data)
        return HttpResponse(pResponse)

def newTime(request):
    if request.method == 'POST':
        data = request.POST.dict()
        tResponse = CF.set_time(data)
        return HttpResponse(tResponse)

def changeAssign(request):
    if request.method == 'GET':
        data = request.GET.dict()
        print("queriendo cambiar",data)
        response = CF.set_assign(data)
        return HttpResponse(response)
#_____________ END CHANGES ________________________________