from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from base.utils import Qlog_user
from athlete.models import Athletes
from competition.models import CompetitionFactory as CF
from .models import ChampionshipInterface as CI, Championships
from .forms import ChampForm


#-----------------FILTER VIEWS ----------------------------

def principalView(request):
    if Qlog_user(request.user):
        return internalPV(request)
    else:
        return externalPV(request)

def allChampionshipsView(request):
    if Qlog_user(request.user):
        return internalACV(request)
    else:
        return externalACV(request)

def reviewChampionship(request,cID):
    if Qlog_user(request.user):
        return internalRC(request,cID)
    else:
        return externalRC(request,cID)

def get_fonts(request):
    if request.method == 'POST':
        data = request.POST.dict()
        folder = os.path.join(FONTS_DIR,data['folder'])
        font_list = os.listdir(folder)
        pos = int(data['value'])
        result = {'value':None,'fontname':None,'style':None,'valid':True}

        if data['function'] == 'next':
            if pos < len(font_list)-1:
                result['fontname'] = font_list[pos+1]
                result['value'] = str(pos+1)
            else:
                result['fontname'] = font_list[pos]
                result['value'] = data['value']

        elif data['function'] == 'previous':
            if pos >0:
                result['fontname'] = font_list[pos-1]
                result['value'] = str(pos-1)
            else:
                result['fontname'] = font_list[pos]
                result['value'] = data['value']

        if 'txt' in result['fontname']:
            result['valid'] = False
        else:
            result['family'] = result['fontname'][:-4]
            #{% static 'fonts\\Montserrat\\%s'%}
            text = "/static/fonts/%s/%s"%(data['folder'],result['fontname'])
            result['style'] = '@font-face {font-family: %s;src: url("%s");}' % (result['family'],text)
            #"@font-face {font-family: examplefont;src: url('{% static 'fonts\\Montserrat\\Montserrat-Black.ttf' %}');}" 
    return JsonResponse(result,safe=False)

#----------------------------------------------------------

#-------------------INTERNAL VIEWS-------------------------
@login_required(login_url=('/'))
def internalPV(request):
    champions = Championships.objects.all().count()
    atles = Athletes.objects.all().count()
    return render(request,'Internal/Principal.html',{'stat_ch':champions,'stat_athle':atles})

@login_required(login_url='/')
def internalACV(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    allchamps = CI.get_all_championships()
    return render(request,'Internal/championships/champslist.html',{'champs':allchamps})

@login_required(login_url=('/'))
def internalRC(request,cID):
    if request.method == 'POST':
        data = request.POST.dict()
        CI.create_stage(data,cID)
    elif request.method == 'GET':
        pass
    champ,stages = CI.get_allfor_championship(cID)
    events = CF.get_all_events()
    return render(request,'Internal/championships/reviewChampionship.html',{'champ':champ,'stages':stages,'events':events})

@login_required(login_url='/')
def newChampionship(request):
    if request.method == 'POST':
        data = request.POST
        form = ChampForm(data)
        if form.is_valid():
             form.is_valid_log()
             CI.create_championship(form.data)
        else:
            print("formulario no valido")
        return redirect('championshipsView')
    elif request.method == 'GET':
        pass
    return render(request,'Internal/championships/newChampionship.html')
#----------------------------------------------------------

#-------------------EXTERNAL VIEWS-------------------------
def externalPV(request):
    return render(request,'External/Principal.html',{'data':'data'})

def externalACV(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    allchamps = CI.get_all_championships()
    return render(request,'External/championships/champslist.html',{'champs':allchamps})

def externalRC(request,cID):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    champ,stages = CI.get_allfor_championship(cID)
    return render(request,'External/championships/reviewChampionship.html',{'champ':champ,'stages':stages})
#----------------------------------------------------------