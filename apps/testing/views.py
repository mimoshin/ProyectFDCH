from django.shortcuts import render
from .forms import NameForm
from championship.models import Championship_Interface, stage_interface, competition_interface
from members.models import athlete_interface
from .models import test_athlete_interface
from .models import test_competition_interface
from .models import test_inscription_interface
from .models import test_championship_interface as I_CHAMP
from .Read_JSON import json_to_list
# Create your views here.

def init_view(request):
    return render(request,'testing/test_generator.html',{'data':'data','usr':''})

def form_test(request):
    if request.method == 'POST':
        print('metodo post')
        form = NameForm(request.POST)
        #result = form.is_valid()
        return render(request,'testing/test_form.html',{'result':form,'usr':''})
    if request.method == 'GET':
        print('metodo get')
        form = NameForm()
        print(form.__str__())
        return render(request,'testing/test_form.html',{'form':form,'usr':''})
    
def inscription_test(request):
    template = 'testing/inscription_test.html'
    competitions = stage_interface.get_all_competitions()
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('amount'):
            id_compt = data['amount'][:-2]
            amount = data['amount'][-2:]
            test_competition_interface.competition_inscription_partial(id_compt,amount)
        elif data.get('remove_insc'):
            print("Eliminar inscripciones de la competencia",data['remove_insc'])
            test_inscription_interface.rm_total_inscriptions(data['remove_insc'])
        elif data.get('remove_series'):
            test_competition_interface.remove_series(data['remove_series'])
        elif data.get('new_series'):
            pass

    elif request.method == 'GET':
        data = request.GET.dict()
        if data.get('competition'):
            competition = competition_interface.get_competition(data['competition'])
            num = athlete_interface.get_athletes_for_compt(competition)
            return render(request,template,{'usr':'','competition':competitions,'total':num})

    return render(request,template,{'usr':'','competition':competitions})


def load_menu(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'testing/load_data/load_menu.html',{'usr':''})

def load_athletes(request):
    athle_list =[]
    if request.method == 'POST':
        data = request.POST.dict()
        print("metodo_post")
        athle_list = json_to_list('new_athletes.json')
        if data.get('category'):
            print("inscribir atletas")
            test_athlete_interface.load_all_athletes(athle_list)
    elif request.method == 'GET':
        print("metodo_get")
    return render(request,'testing/load_data/load_athletes.html',{'usr':'','athletes':athle_list})

def load_clubs(request):
    clubs_list=[]
    if request.method == 'POST':
        clubs_list = json_to_list('clubs.json')
        #test_competition_interface.load_all_clubs(clubs_list)
    if request.method == 'GET':
        pass
    return render(request,'testing/load_data/load_clubs.html',{'usr':'','clubs':clubs_list})

def load_championships(request):
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('champs'):
            I_CHAMP.load_championships()
        elif data.get('stages'):
            I_CHAMP.load_stages()
    if request.method == 'GET':
        pass
    return render(request,'testing/load_data/load_championships.html',{'usr':''})