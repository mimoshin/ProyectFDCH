from django.shortcuts import redirect, render
from .models import interfaz

# Create your views here.
def cargar_excel(request):
    interfaz.cargar_excel()
    return redirect('test_principal')
    
def cargar_horario(request):
    interfaz.cargar_hora()
    return redirect('test_principal')

def mostrar_datos(request):
    data = interfaz.cargar_todo()
    if request.method == 'GET':
        ddd= request.GET.dict()
        if ddd.get('prueba'):
            data = interfaz.filtrar(ddd['prueba'],ddd['gender'])
            return render(request,'MuestraCarga.html',{'data':data})
    return render(request,'MuestraCarga.html',{'data':data})