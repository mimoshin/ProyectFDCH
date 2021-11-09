from django import http
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import athlete, athlete_interface
from championship.models import Championship_Interface, stage_interface

# Create your views here.
def athletes_view(request):
    user = request.user
    if str(user.__class__()) == 'AnonymousUser':
        return general_athletes_view(request)
    elif user.super_admin_set.exists():
        return admin_athletes_view(request)
    return redirect('principal')

def general_athletes_view(request):
    athletes = []
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = request.GET.dict()
        athletes = athlete_interface.get_filter(form)
    elif not athletes:
        athletes = 'EMPTY'
    return render(request,'members/external_athletes.html',{'athletes':athletes,'pagination':False})
    
def admin_athletes_view(request):
    athletes = []
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = request.GET
        athletes = athlete_interface.get_filter(form)
        if not athletes:
            athletes = 'EMPTY'
    return render(request,'members/external_athletes.html',{'athletes':athletes})

def athletes_inscription(request,c_id):
    champ = Championship_Interface.get_championship(c_id)
    compts = stage_interface.get_champ_activitys(c_id)
    athletes = []
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = request.GET
        athletes = athlete_interface.get_filter(form)
        if not athletes:
            athletes = 'EMPTY'
    return render(request,'members/athletes_inscription.html',{'champ':champ,'competitions':compts,'athletes':athletes,'usr':''})

def Question(request):
    if request.method == 'POST':
        form = request.POST
        a_list = list(athlete_interface.get_filter(form).values_list())
        return JsonResponse(a_list,safe=False)
    elif request.method == 'GET':
        print(request.GET)
        return HttpResponse('hola')

def load_data(request):
    if request.method == 'POST':
        athlete_interface.new_load_athletes()
    elif request.method == 'GET':
        pass
    return redirect('stats')

def inscription(request):
    if request.method == 'POST':
        print(request.POST)
    elif request.method == 'GET':
        pass
    print(request)
    return redirect('principal')

def alternative(request):
    if request.method == 'POST':
        data_dict = request.POST.dict()
        print(data_dict)
        data_list = list(request.POST)
        #print(data_list)
        id_comp, compts = [], []
        atleta = request.POST['athlete']
        for x in data_list:
            if 'COMPT' in x:
                cpk = x.split('-')[1]
                id_comp.append(cpk)
        
        for a in id_comp:
            compts.append(stage_interface.get_competition(a))
        for x in id_comp:
            stage_interface.new_inscription(atleta,x)

        print("atleta %s queriendo inscribirse a las pruebas:" %(atleta))
        for b in compts:
            print(b.pk)
            
        return redirect('/atletas/inscripcion/33?name=&category=1')
    return redirect('principal')

def delete_all(request):
    if request.method == 'POST':
        athlete_interface.delete_all_athletes()
    elif request.method == 'GET':
        pass
    return redirect('stats')

def query_compt(request):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        data = request.GET.dict()
        if data['obj'] == 'load_compt':
            print("consultando para cargar pruebas",data)
            data = stage_interface.get_competitions_filter(data['champ'],data['category'],data['gender'],data['atle'])
        return HttpResponse(data)
        
    return redirect('stats')