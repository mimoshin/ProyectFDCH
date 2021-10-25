from django.shortcuts import redirect, render
from .read_json import json_to_list
from .models import Track_Interface as T_I

# Create your views here.
def principal(request):
    return render(request,'principal/principal.html',{'usr':''})


def results_view(request):
    rlist = []
    champs = CI.get_all_champs()
    if request.method == 'POST':
        data = request.POST.dict()
    elif request.method == 'GET':
        data = request.GET.dict()
        if data.get('options'):
            rlist = T_I.load_results(data['options'])
    return render(request,'results.html',{'usr':'','results':rlist,'champs':champs})

def load_results(request,c_id):
    T_I.charge_results(c_id)
    return redirect('results_view')
    
def delete_results(request,c_id):
    T_I.delete_results(c_id)
    return redirect('results_view')

def athletes_view(request):
    if request.method == 'POST':
        print(request.POST)
    elif request.method == 'GET':
        pass
    return render(request,'athletes.html',{'usr':'','athletes':''})



