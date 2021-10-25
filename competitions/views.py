from os import times
from django.apps.registry import apps
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from base.utils import get_fields
from .models import jumpInterface, newInterface, throwInterface, trackInterface as TI
from .models import competitionInterface as CTI

    
# Create your views here.
def principal_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('review_rut'):
            print("Comprobar los rut en los resultados")
    elif request.method == 'GET':
        pass
    return render(request,'comptAdmin/comPrincipal.html',{'usr':''})

def load_sports(request):
    CTI.load_sports()
    return redirect('compt_principal')

def delete_sports(request):
    CTI.delete_sports()
    return redirect('compt_principal')

def load_competitions(request):
    CTI.load_competitions()
    return redirect('compt_principal')

def delete_competitions(request):
    CTI.delete_competitions
    return redirect('compt_principal')

def load_trackhead2s(request):
    TI.load_trackhead2s()
    return redirect('track_principal')

def delete_trackhead2s(request):
    TI.delete_trackhead2s()
    return redirect('track_principal')

def load_track2s(request):
    TI.load_track2s('5000_RESULTS.json')
    TI.load_track2s('10000_RESULTS.json')
    return redirect('track_principal')

def load_resume(request):
    newInterface.load_new_results('5000_RESULTS.json')
    newInterface.load_new_results('10000_RESULTS.json')
    return redirect('track_principal')

def delete_resume(request):
    newInterface.delete_new_results()
    return redirect('track_principal')

def delete_track2s(request):
    TI.delete_track2s()
    return redirect('track_principal')

def compare(request):
    newInterface.compare()
    return redirect('track_principal')

def load_resume_trhow(request):
    throwInterface.load_resumeThrow('throw2s.json')
    return redirect('track_principal')

def delete_resume_trhow(request):
    throwInterface.delete_resumeThrow()
    return redirect('track_principal')

def load_resume_jump(request):
    jumpInterface.load_resumeJump('hjump2s.json')
    jumpInterface.load_resumeJump('jump2s.json')
    return redirect('track_principal')

def delete_resume_jump(request):
    jumpInterface.delete_resumeJump()
    return redirect('track_principal')



def track_principal(request):
    models_head = get_fields('competitions','track_head2s')
    models_track = get_fields('competitions','track2s')
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('results'):
            TI.review_results()
            return HttpResponse("hola")
        if data.get('anames'):
            newInterface.repair_athletes('throw')
            return HttpResponse("hola")
    elif request.method == 'GET':
        pass
    return render(request,'comptAdmin/tracksPrincipal.html',{'usr':'','model1':models_head,'model2':models_track})

def throw_principal(request):
    models_head = get_fields('competitions','track_head2s')
    models_track = get_fields('competitions','track2s')
   
    return render(request,'comptAdmin/throwPrincipal.html',{'usr':'','model1':models_head,'model2':models_track})

def jump_principal(request):
    models_head = get_fields('competitions','track_head2s')
    models_track = get_fields('competitions','track2s')
   
    return render(request,'comptAdmin/jumpPrincipal.html',{'usr':'','model1':models_head,'model2':models_track})



def view_results(request,compt):
    data = 'hola'
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        print("request_GET",request.GET)
    return render(request,"comptAdmin/resultsPrincipal.html",{'usr':'','data':data})
