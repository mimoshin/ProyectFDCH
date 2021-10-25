from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect, render
from .models import asbtractInterface as AI

# Create your views here.

def principal_view(request):
    return render(request,'otherAdmin/otherPrincipal.html',{'usr':''})

def load_categories(request):
    AI.load_categories()
    return redirect('other_principal')

def delete_categories(request):
    AI.delete_categories()
    return redirect('other_principal')

def load_sexes(request):
    AI.load_sexes()
    return redirect('other_principal')

def delete_sexes(request):
    AI.delete_sexes()
    return redirect('other_principal')