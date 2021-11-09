from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Championship_Interface, inscription, serie, stage_interface, generator, series_interface, test
from .forms import ChampForm

#::::general_views:::::::::

def championship_view(request):
    user = request.user
    if str(user.__class__()) == 'AnonymousUser':
        return championship_general_view(request)
    elif user.super_admin_set.exists():
        return championship_admin_view(request)
    return redirect('principal')

def championship_general_view(request):
    champs = Championship_Interface.get_all_championships()
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'External/championship/eChampionshipView.html',{'champs':champs})

def review_championship(request,c_id):
    user = request.user
    if str(user.__class__()) == 'AnonymousUser':
        return general_review_championship(request,c_id)
    elif user.super_admin_set.exists():
         return admin_review_championship(request,c_id)
    return redirect('principal')
    
def general_review_championship(request,c_id):
    champ = Championship_Interface.get_championship(c_id)
    if request.method == 'POST':
        return redirect('review_champ',c_id)
    elif request.method == 'GET':
        pass
    stages,competitions = stage_interface.get_championship_data(champ)   
    return render(request,'External/championship/eReviewChampionship.html',{'champ':champ,'stage':stages,'activitys':competitions})

def new_championship(request):
    new_c = ChampForm()
    if request.method == 'POST':
        
        data = request.POST
        form = ChampForm(data)
        if form.is_valid():
             form.is_valid_log()
             Championship_Interface.create_championship(form.data)
        
        return redirect('new_champ')
    elif request.method == 'GET':
        pass
    return render(request,'Internal/championship/iNewChampionship.html',{'usr':'','formulario':new_c})


def generate_activitys(request):
    generator.create_competitions()
    return redirect('new_champ')

def new_competition(request,stage_id):
    if request.method == 'POST':
        result = stage_interface.new_compt(stage_id,request.POST)
        return HttpResponse(result)
    elif request.method == 'GET':
        pass

def review_competition(request,c_id):
    user = request.user
    if str(user.__class__()) == 'AnonymousUser':
        return general_review_competition(request,c_id)
    elif user.super_admin_set.exists():
        return admin_review_competition(request,c_id)
    return redirect('principal')

def general_review_competition(request,c_id):
    competition = stage_interface.get_competition(c_id)
    inscriptions = stage_interface.get_inscriptions_compt(c_id)
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'External/championship/eCompetitionView.html',{'data':competition,'inscriptions':inscriptions})

#::::end_general_views:::::

#::::admin_views:::::::::::
def championship_admin_view(request):
    champs = Championship_Interface.get_all_championships()
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'Internal/championship/iChampionshipView.html',{'champs':champs,'usr':''})

def admin_review_championship(request,c_id):
    champ = Championship_Interface.get_championship(c_id)
    if request.method == 'POST':
        stage_interface.create_stage(request.POST,c_id)
        return redirect('review_champ',c_id)
    elif request.method == 'GET':
        pass
    stages,competitions = stage_interface.get_complete_stages(champ)
    tests =  test.objects.all()
    return render(request,'Internal/championship/iReviewChampionship.html',{'champ':champ,'stage':stages,'activitys':competitions,'usr':'','tests':tests})

def admin_review_competition(request,c_id):
    template = {0:'championship/admin_view_track_competition.html',
                1:'championship/admin_view_jump_competition.html',
                2:'championship/admin_view_throw_competition.html'}

    competition = stage_interface.get_competition(c_id)
    t_type = int(competition.get_type()) 

    if request.method == 'POST':
        print("POST:",request.POST)
        data = request.POST.dict()
        series_interface.new_series(competition,data['total'])
        #print("buscar los atletas inscritos a la competencia: ",len(inscriptions))
        #print("del total de atletas dividirlos por la cantidad indicada y crear las series correspondientes")
        #print("luego asignar a los atletas a las series")
    elif request.method == 'GET':
        if competition.series:
            print("series creadas, cargar series")
            total_series = series_interface.get_series(c_id)
            print('total_series',total_series)
            return render(request,template[t_type],{'data':competition,'inscriptions':False,'series':total_series,'usr':''})
        else:
            inscriptions = stage_interface.get_inscriptions_compt(c_id)
            print("Inscripciones",inscriptions)
            return render(request,template[t_type],{'data':competition,'inscriptions':inscriptions,'usr':''})
    return render(request,template[t_type],{'data':competition,'inscriptions':False,'usr':''})
     

#::::end_admin_views:::::::