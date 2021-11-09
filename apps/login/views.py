from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from stadistics.models import champ_stadistics, athletes_stadistics
from championship.models import inscription, competition
from members.models import athlete

# Create your views here.
def init_view(request):
    champs = champ_stadistics.objects.last()
    athles = athletes_stadistics.objects.last()
    athles.num_athletes = athlete.objects.count()
    athles.save()

    compet = inscription.objects.count()
    cienh = inscription.objects.filter(compt_fk__test_fk__test_name='100 METROS PLANOS',compt_fk__gender=2).count()
    cienm = inscription.objects.filter(compt_fk__test_fk__test_name='100 METROS PLANOS',compt_fk__gender=1).count()  
    realizeds = competition.objects.count()

    user = request.user
    cls = str(user.__class__())
    template_name = {'AnonymousUser':'principal.html','admin':'admin_principal.html'}
    if cls == 'AnonymousUser':
        print('cargar vista con AnonymousUser')
    elif user.super_admin_set.exists():
        return render(request,template_name['admin'],
        {'usr':cls,'stat_ch':champs,'stat_athle':athles,'compts':compet,'reali':realizeds,'cienh':cienh,'cienm':cienm})
    return render(request,template_name[cls],
        {'usr':cls,'stat_ch':champs,'stat_athle':athles,'compts':compet,'reali':realizeds,'cienh':cienh,'cienm':cienm})

def login_view(request):
    if request.method == 'POST':
        username,password = request.POST['username'],request.POST['password']
        user_auth = authenticate(username=username,password=password)# T:User | F:None 
        if user_auth:
            login(request,user_auth)
            return redirect('principal')
        else:
            print("introducir mensajes de alerta")

    if request.method == 'GET':
        usr = str(request.user.__class__())
        if usr == 'AnonymousUser':#usuario anonimo 
            return render(request,'Login/login.html') 
        else: #usuario logeado
            return redirect('principal') 

    logout(request)#terminar cualquier inicio de sesion
    return render(request,'login/login.html')

def user_logout(request):
    logout(request)
    return redirect('principal')
#::::::general_views:::::::::
#::::::end_general_views:::::

#::::::admin_views::::::::::
#::::::end_admin_views::::::
