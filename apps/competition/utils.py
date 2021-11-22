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