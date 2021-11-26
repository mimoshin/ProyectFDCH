from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect 
from base.settings import DATABASES
from base.utils import Qlog_user
from athlete.models import Athletes, AthleteInterface as AI
from login.models import UserFactory as UF
from competition.models import CompetitionFactory as CF
from .models import ChampionshipInterface as CI, Championships
from .models import ChampionshipFactory as CHF
from .forms import ChampForm


#-----------------FILTER VIEWS ----------------------------
def principalView(request):
    if Qlog_user(request.user):
        options = {'Fedachi':fedachiPV,False:internalPV}
        user = UF.get_type_user2(request.user)
        return options[user](request)
    else:
        return externalPV(request)

def allChampionshipsView(request):
    if Qlog_user(request.user):
        options = {'Fedachi':fedachiACV,False:internalACV}
        user = UF.get_type_user2(request.user)
        return options[user](request)
    else:
        return externalACV(request)

def reviewChampionship(request,cID):
    if Qlog_user(request.user):
        options = {'Fedachi':fedachiRC,False:internalRC}
        user = UF.get_type_user2(request.user)
        return options[user](request,cID)
    else:
        return externalRC(request,cID)
#----------------------------------------------------------

#-------------------INTERNAL VIEWS-------------------------
@login_required(login_url=('/'))
def internalPV(request):
    champions = Championships.objects.all().count()
    atles = Athletes.objects.all().count()
    return render(request,'Internal/principal.html',{'stat_ch':champions,'stat_athle':atles})

@login_required(login_url='/')
def internalACV(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    allchamps = CHF.get_all_championships()
    #allchamps = CI.get_all_championships()
    return render(request,'Internal/championships/champslist.html',{'champs':allchamps})

@login_required(login_url=('/'))
def internalRC(request,cID):
    if request.method == 'POST':
        data = request.POST.dict()
        #CI.create_stage(data,cID)
        CHF.create_stage
    elif request.method == 'GET':
        pass
    champ,stages = CHF.get_allfor_championship(cID)
    #champ,stages = CI.get_allfor_championship(cID)
    events = CF.get_all_events()
    return render(request,'Internal/championships/reviewChampionship.html',{'champ':champ,'stages':stages,'events':events})

@login_required(login_url='/')
def newChampionship(request):
    data = {'user':''}
    user = UF.get_type_user(request.user)
    data['user'] = user[1]
    
    if request.method == 'POST':
        data = request.POST
        form = ChampForm(data)
        if form.is_valid():
             form.is_valid_log()
             CHF.create_championship(form.data)
             #CI.create_championship(form.data)
        else:
            print("formulario no valido")
        return redirect('championshipsView')
    elif request.method == 'GET':
        pass
    return render(request,'Internal/championships/newChampionship.html',data)
#----------------------------------------------------------

#-------------------EXTERNAL VIEWS-------------------------
def externalPV(request):
    champs_count = CHF.get_all_championships().count()
    athletes_count = AI.get_all_athletes().count()
    return render(request,'External/principal.html',{'champs':champs_count,'athletes':athletes_count})

def externalACV(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    allchamps = CI.get_all_championships()
    actives = allchamps.filter(status=1)
    return render(request,'External/championships/champslist.html',{'champs':actives})

def externalRC(request,cID):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    champ,stages = CI.get_allfor_championship(cID)
    return render(request,'External/championships/reviewChampionship.html',{'champ':champ,'stages':stages})
#----------------------------------------------------------

#--------------------FedachiViews-------------------------------------

@login_required(login_url='/')
def fedachiPV(request):
    champs_count = CHF.get_all_championships().count()
    athletes_count = AI.get_all_athletes().count()
    return render(request,"Internal/principal.html",{'champs':champs_count,'athletes':athletes_count})

@login_required(login_url='/')
def fedachiACV(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    allchamps = CI.get_all_championships()
    return render(request,"Internal/championships/champslist.html",{'champs':allchamps})
    #return render(request,"members/FedachiUser/championships/champslist.html",{'champs':allchamps})


@login_required(login_url=('/'))
def fedachiRC(request,cID):
    if request.method == 'POST':
        data = request.POST.dict()
        CI.create_stage(data,cID)
    elif request.method == 'GET':
        pass
    champ,stages = CI.get_allfor_championship(cID)
    events = CF.get_all_events()
    return render(request,'members/FedachiUser/championships/reviewChampionship.html',{'champ':champ,'stages':stages,'events':events})

#_____________ QUERYS ____________________________________
@login_required(login_url=('/'))
def QFChampionship(request):
    #cargar todas los torneos
    if request.method == 'GET':
        data = request.GET.dict()
        champ,stages = CHF.get_champ_and_stages(data['id'])
        if data.get('cStatus'):
            champ.not_status()
        dataT = {'champ':champ,'stages':stages}
        template = 'members/FedachiUser/championships/champsData.html'
        return render(request,template,dataT)

@login_required(login_url=('/'))        
def QFDisable(request):
    if request.method == 'GET':
        data = request.GET.dict()
        CHF.disable_stage(data['id'])
        return HttpResponse(True)
        #return redirect('fedachi_championships')

#_____________ END QUERYS _________________________________

#_____________ CHANGES _________________________________

@login_required(login_url='/')
def modifyChampionship(request,champID):
    data = {'user':''}
    user = UF.get_type_user(request.user)
    data['user'] = user[1]
    if request.method == 'POST':
        data = request.POST.dict()
        CHF.modify_championship(champID,data)
        return redirect('championshipsView')
    elif request.method == 'GET':
        data['champ'] = CHF.get_championship(champID)
    return render(request,'Internal/championships/modifyChampionship.html',data)

@login_required(login_url=('/'))
def newStage(request,champID):
    if request.method == 'POST':
        data = request.POST.dict()
        CHF.create_stage(data,champID)
        return redirect('fedachi_championships',{'user':'data'})
#_____________ END CHANGES _________________________________

def handler404(request, exception, template_name="404.html"):
    return redirect('principalView')

def errorView(request, exception, template_name="404.html"):
    return redirect('principalView')
"""

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
    /*Funcion para cambiar la fuente del texto
        primeramente se elige la carpeta que hace alusion a la fuente en cuestion
        luego se eligue cambiar mediante los botones los distintos archivos de fuente
        $('#select').change(function(){
            btns = $('.options');
            btns[0].value = 0;
            btns[1].value = 0;   
        });
    
        $('.options').on('click',function(){
            btns = $('.options');
            select = $('#select').val();
            $.post( "{% url 'get_fonts' %}",
                    {'csrfmiddlewaretoken':'{{csrf_token}}','folder':select,'function':this.id,'value':this.value},
                    function(response){
                        if(response['valid']){
                            $('style')[0].innerText = '';
                            $("style").append(response['style']);
                            $("style").append(".hola{font-family:"+response['family']+";}");
                            console.log(response['style']);
                        }
                        btns[0].value = response['value'];
                        btns[1].value = response['value'];   
                    }
            );
        });*/
"""

