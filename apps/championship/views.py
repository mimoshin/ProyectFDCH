from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Championship_Interface, stage_interface, generator



#::::general_views:::::::::
def championship_view(request):
    user = request.user
    if str(user.__class__()) == 'AnonymousUser':
        return championship_general_view(request)
    elif user.superadmin_set.exists():
        return championship_admin_view(request)
    return redirect('principal')

def championship_general_view(request):
    champs = Championship_Interface.get_all_championships()
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'championship/external_championship_view.html',{'champs':champs})

def review_championship(request,c_id):
    user = request.user
    if str(user.__class__()) == 'AnonymousUser':
        return general_review_championship(request,c_id)
    elif user.superadmin_set.exists():
         return admin_review_championship(request,c_id)
    return redirect('principal')
    
def general_review_championship(request,c_id):
    champ = Championship_Interface.get_championship(c_id)
    if request.method == 'POST':
        return redirect('review_champ',c_id)
    elif request.method == 'GET':
        pass
    stages,competitions = stage_interface.get_championship_data(champ)   
    return render(request,'championship/external_review_championship.html',{'champ':champ,'stage':stages,'activitys':competitions})

def new_championship(request):
    if request.method == 'POST':
        Championship_Interface.create_championship(request.POST)
        return redirect('championships')
    elif request.method == 'GET':
        pass
    return render(request,'championship/admin_new_championship.html')


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
    elif user.superadmin_set.exists():
        return admin_review_competition(request,c_id)
    return redirect('principal')

def general_review_competition(request,c_id):
    competition = stage_interface.get_competition(c_id)
    inscriptions = stage_interface.get_inscriptions(c_id)
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'championship/external_view_competition.html',{'data':competition,'inscriptions':inscriptions})

#::::end_general_views:::::

#::::admin_views:::::::::::
def championship_admin_view(request):
    champs = Championship_Interface.get_all_championships()
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'championship/admin_championship_view.html',{'champs':champs,'usr':''})

def admin_review_championship(request,c_id):
    champ = Championship_Interface.get_championship(c_id)
    if request.method == 'POST':
        stage_interface.create_stage(request.POST,c_id)
        return redirect('review_champ',c_id)
    elif request.method == 'GET':
        pass
    stages,competitions = stage_interface.get_complete_stages(champ)   
    return render(request,'championship/admin_review_championship.html',{'champ':champ,'stage':stages,'activitys':competitions,'usr':''})

def admin_review_competition(request,c_id):
    competition = stage_interface.get_competition(c_id)
    inscriptions = stage_interface.get_inscriptions(c_id)
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return render(request,'championship/admin_view_competition.html',{'data':competition,'inscriptions':inscriptions,'usr':''})


#::::end_admin_views:::::::