from django.contrib.auth.decorators import login_required
from openpyxl import Workbook as WB, load_workbook as LD_W
from django.http.response import HttpResponse,FileResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, View
from base.utils import get_fonts,Qlog_user
from base.const import FEDACHI_LOGO
from .models import competitionInterface as CI, competitions, events, mdHeats, speedAssignments
from .utils import renderPDF

def starlist_view(request,cp_id):
    if Qlog_user(request.user):
        return internal_SV(request,cp_id)
    else:
        return external_SV(request,cp_id)

def external_SV(request,cp_id):
    #client_view
    templates = {1:'External/competition/eStartlistSP.html',2:'External/competition/eStartlistMD.html',
                3:'External/competition/eStartlistJP.html',4:'External/competition/eStartlistPV.html',5:'External/competition/eStartlistTW.html'}
    
    competition = CI.get_competition(cp_id)
    ctype = competition.type()
    heats = CI.get_heats(cp_id,ctype)
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,templates[ctype],{'data':'data','id':cp_id,'competition':competition,'heats_data':heats})

@login_required(login_url=('/'))
def internal_SV(request,cp_id):
    #fonts = get_fonts()
    #admin_view
    templates = {1:'Internal/competition/iStartlistSP.html',2:'Internal/competition/iStartlistMD.html',
                3:'Internal/competition/iStartlistJP.html',4:'Internal/competition/iStartlistPV.html',5:'Internal/competition/iStartlistTW.html'}
    competition = CI.get_competition(cp_id)
    ctype = competition.type()
    heats = CI.get_heats(cp_id,ctype)
    if request.method == 'POST':
        data = request.POST.dict()
        print("recibiendo data",data)
    elif request.method == 'GET':
        pass
    return render(request,templates[ctype],{'data':'data','id':cp_id,'competition':competition,'heats_data':heats})

def results_view(request,cp_id):
    if Qlog_user(request.user):
        return internal_RV(request,cp_id)
    else:
        return external_RV(request,cp_id)

def external_RV(request,cp_id):
    #client_view
    templates = {1:'External/competition/eResultsSP.html',2:'External/competition/eResultsMD.html',
                3:'External/competition/eResultsJP.html',4:'External/competition/eResultsPV.html',5:'External/competition/eResultsTW.html'}
    competition = CI.get_competition(cp_id)
    ctype = competition.type()
    heats = CI.get_heats(cp_id,ctype)
    return render(request,templates[ctype],{'id':cp_id,'competition':competition,'heats_data':heats})

@login_required(login_url='/')
def internal_RV(request,cp_id):
    #admin_view
    #fonts = get_fonts()
    templates = {1:'Internal/competition/iResultsSP.html',2:'Internal/competition/iResultsMD.html',
                3:'Internal/competition/iResultsJP.html',4:'Internal/competition/iResultsPV.html',5:'Internal/competition/iResultsTW.html'}
    competition = CI.get_competition(cp_id)
    ctype = competition.type()
    heats = CI.get_heats(cp_id,ctype)
    return render(request,templates[ctype],{'id':cp_id,'competition':competition,'heats_data':heats})


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
    competition = CI.get_competition(Type)
    print(competition)
    excel = competition.file()
    response = FileResponse(open('static\\files\\'+excel,'wb+'))
    return response

def download_results(request,Type):
    wb = WB()
    wb.save('static\\files\\archivo.xlsx')
    #Retorna el archivo para su descarga
    #Implementar: Generacion de archivo con las series y el nombre de la prueba
    competition = CI.get_competition(Type)
    excel = competition.file()
    response = FileResponse(open('static\\files\\archivo.xlsx','rb'))
    return response

def template(request):
    renderPDF('competition/startlist.html','hola')
    return redirect('principal')

class startView(ListView):
    model = speedAssignments
    template_name = 'competition/descargar.html'
    context_object_name = 'series'

class otroview(View):
    def get(self,request,*args,**kwargs):
        templates = {1:'competition/lista.html'}
        competition = CI.get_competition(1)
        heats = CI.get_heats(1,1)
        data = {'competition':competition,'heats':heats,'url':FEDACHI_LOGO}
        pdf = renderPDF(templates[1],data)
        return HttpResponse(pdf,content_type='application/pdf')


def pdfView(request,c_id):
    templates = {1:'competition/lista.html',2:'competition/docs/mdST.html',
                 3:'competition/docs/jumpST.html',4:'competition/docs/hjumpST.html',5:'competition/docs/throwST.html'}
    if request.method == 'GET':
        competition = CI.get_competition(c_id)
        heats = CI.get_heats(c_id,1)
        data = {'competition':competition,'heats':heats,'url':FEDACHI_LOGO}
        pdf = renderPDF(templates[competition.type()],data)
        return HttpResponse(pdf,content_type='application/pdf')
