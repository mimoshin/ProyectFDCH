from django.shortcuts import redirect, render
from base.utils import get_fields
from .models import championshipInterface as CI

# Create your views here.
def principal_view(request):
    champ_model = get_fields('championships','championship')
    stage_model = get_fields('championships','stage')
    regh_model = get_fields('championships','registration_head2')
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass 
    return render(request,'champAdmin/champPrincipal.html',{'usr':'',
                'model1':champ_model[2:],'model2':stage_model,'model3':regh_model})

def load_championships(request):
    CI.load_championships()
    return redirect('champ_principal')

def delete_championship(request):
    CI.delete_championships()
    return redirect('champ_principal')

def load_stages(request):
    CI.load_stages()
    return redirect('champ_principal')

def delete_stages(request):
    CI.delete_stages()
    return redirect('champ_principal')

def load_registrations(request):
    CI.load_registrationheads()
    return redirect('champ_principal')

def delete_registrations(request):
    CI.delete_registrationheads()
    return redirect('champ_principal')