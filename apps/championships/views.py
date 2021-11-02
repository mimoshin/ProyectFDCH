import os
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from base.settings import FONTS_DIR
from base.utils import Qlog_user
from .models import championshipInterface as CI


#-------------PRINCIPAL VIEWS------------------------------
def principal_view(request):
    if Qlog_user(request.user):
        return internal_PV(request)
    else:
        return external_PV(request)
    
def external_PV(request):
    #client_view
    print("cargado externalPV")
    champ,stages = CI.get_total_champ(86)
    return render(request,'External/ePrincipal.html',{'stage':stages,'champ':champ,'data':'data'})

@login_required(login_url='/')
def internal_PV(request):
    #admins_view
    champ,stages = CI.get_total_champ(86)
    return render(request,'Internal/iPrincipal.html',{'stage':stages,'champ':champ,'data':'data'})


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