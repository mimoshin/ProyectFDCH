from io import BytesIO
from django.http import response
from django.http.request import HttpHeaders
from django.http.response import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template


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
            