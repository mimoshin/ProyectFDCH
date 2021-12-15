from os import truncate
import re
from io import BytesIO
from typing import Optional, Text
from django.http.response import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template


#Formato SPEED-JUMP-THROW re.search("^[0-9]{1,3}\.[0-9]{1,3}$",a)
#Formato MID re.search("^[0-9]{1,3}\:[0-9]{2}\.[0-9]{1,4}$",a)
#Formato wind re.search("^\-|\+[0-9]{1,2}\.[0-9]{1,3}$",a)

def renderPDF(template_src,context):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(),content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename='hola.pdf'"
        return response


def orderTimesSpeed(datalist):
    times = []
    for x in datalist:
        result = float(x.result)
        times.append({x.id:result})

    total = len(times)

    for index in range(total):      
        for  indexb in range(total):
            aux = times[index]
            auxid = None
            auxres = None
            for a,b in aux.items():
                auxid = a
                auxres = b  
                equis = times[indexb]
            zid = None
            zres = None
            for a,b in equis.items():
                zid = a
                zres = b
            if zres > auxres:
                times[index] = equis
                times[indexb] = aux
    print(times)

    for item in datalist:
        for x in range(total):
            aux = times[x]
            for a,b in aux.items():
                auxid = a
            if auxid == item.id:
                print("Atleta %s en el puesto %s"%(item.id,x))
                item.place = x+1
                item.save()
    
def best_time_throw(dataList):
    #Determina mejor marca en lanzamiento
    bestresult = 0
    for x in dataList:
        if x.result != 'x' and x.result != 'X':
            if bestresult == 0:
                bestresult = float(x.result)
            elif float(x.result) > bestresult:
                bestresult = float(x.result)
    return bestresult

def best_jump(dataList):
    bestresult = 0
    for x in dataList:
        if x.result != 'x' and x.result != 'X':
            if bestresult == 0:
                bestresult = float(x.result)
            elif float(x.result) > bestresult:
                bestresult = float(x.result)
    return bestresult

def order_throw_places(dataList):
    total = len(dataList)
    aux = []
    default = []
    for x in dataList:
        a = re.search("^[0-9].*[0-9]$",x['result'])
        if a:
            aux.append(x)
        else:
            default.append(x)

    total = len(aux)
    for index in range(total,0,-1):
        for i in range(index):
            if i < index-1:
                uno = float(aux[i]['result'])
                dos = float(aux[i+1]['result'])
                if uno < dos :
                    piv = aux[i]
                    aux[i] = aux[i+1]
                    aux[i+1] = piv
    return aux,default

def validate_data(data):
    text= data['participation']
    pType = data['type']
    if data.get('wind') or data.get('wind') == '':
        return validate_datas(text,pType) and validate_datas(data['wind'],'wind')
    else:
        return validate_datas(text,pType)

def validate_datas(text,pType):
    if pType == 'wind':
        a = re.search("^\-|\+[0-9]{1,2}\.[0-9]{1,3}$",text)
    elif pType == '1' or pType == '2':
        a = re.search("^[0-9]{1,3}\.[0-9]{1,3}$",text)
    elif pType == '3':
        a = re.search("^[0-9]{1,3}\:[0-9]{2}\.[0-9]{1,4}$",text)
    if a:
        return True
    elif text.upper() in ['DNS','DNF','DQ','X','-','0']:
        return True
    else:
        return False


##REVISAR USO
def validate_data_wind(wind):
    print("comprobar viento")
    if wind == ' ' or wind == '0':
        return True
    else:
        b = re.search("^\-|\+[0-9]{1,2}\.[0-9]{1,3}$",wind)
        if b:
            print("viento validos",wind)
            return True
    return False

def validate_data_wind(wind):
    print("comprobar viento")
    if wind == ' ' or wind == '0':
        return True
    else:
        b,c = re.search("^\+[0-9]{1,2}\.[0-9]{1,3}$",wind),re.search("^\-[0-9]{1,2}\.[0-9]{1,3}$",wind)
        if b or c:
            print("viento validos",wind)
            return True
    return False

def validate_dataxx(data):
    if data['type'] == '1':
        return (validate_data_jump(data['participation']) and validate_data_wind(data['wind']))
    if data['type'] == '2':
        return validate_data_throw(data['participation'])

def validate_data_throw(text):
    aceptados = ['DNS','DNF','DQ']
    if text.upper() in aceptados:
        return True
    elif text.upper() == 'X':
        return True
    else:
        b,c = re.search("^[0-9]{1,3}\.[0-9]{1,3}$",text),re.search("^[0-9]{1,3}$",text)
        if b or c:
            return True
        else:
            return False

def validate_data_jump(participation):
    aceptados = ['DNS','DNF','DQ']
    if participation.upper() in aceptados:
        return True
    elif participation.upper() == 'X':
        return True
    else:
        b,c = re.search("^[0-9]{1,2}\.[0-9]{1,3}$",participation),re.search("^[0-9]{1,3}$",participation)
        if b or c:
            return True
        else:
            return False