from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from base.utils import get_fields
from develop.read_json import json_to_list,write_json
from .models import athleteInterface as AI

# Create your views here.

def principal_view(request):
    attr_model = get_fields('athletes','athlete')

    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('review_names'):
            # revisa los nombres mas escritos y obtiene un resumen de errores en ellos
            result = AI.review_names()
            return JsonResponse(result, safe=False)
        elif data.get('review_rut'):
            result = AI.review_rut()
            return JsonResponse(result, safe=False)
        elif data.get('new_json'):
            AI.gen_json()
            HttpResponse("hola")
    else:
        pass
    return render(request,'athleAdmin/athleprincipal.html',{'usr':'','attrs':attr_model})

def repair_names(request):
    athletes = AI.all_athletes()
    AI.repair_names(athletes,'names')
    AI.repair_names(athletes,'surnames')
    return redirect('atle_principal')

def repair_ruts(request):
    athletes = AI.all_athletes()
    AI.repair_ruts(athletes)
    return redirect('atle_principal')

def load_athletes(request):
    athletes = json_to_list('athletes.json')
    AI.load_athletes(athletes)
    return redirect('atle_principal')

def delete_athletes(request):
    AI.delete_all_athletes()
    return redirect('atle_principal')

def view_athletes(request):
    athletes = AI.all_athletes()
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('news'):
            write_json(AI.new_athletes(athletes))
    elif request.method == 'GET':
        pass
    return render(request,'athletes2.html',{'usr':'','athletes':athletes})