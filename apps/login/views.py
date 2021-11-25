from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from base.utils import Qlog_user


def logView(request):
    if request.method == 'POST':
        #recepción de formulario
        data = request.POST.dict()
        if data.get('username') and data.get('password'):
            username,password = data['username'],data['password']
            user_auth = authenticate(username=username,password=password)
            if user_auth:
                login(request,user_auth)
                return redirect('principalView')

    elif request.method == 'GET':
        #redirección de usuario
        if Qlog_user(request.user):
            return redirect('principalView')
        else:
            return render(request,'login/login.html')
    return redirect('login')

def logoutView(request):
    #cerrar sesión
    logout(request)
    return redirect('principalView')

