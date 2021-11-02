import random
from apps.competitions.utils import renderPDF
from django.shortcuts import redirect, render
from .models import athleteInterface as AI, championshipInterface as CI, competitionInterface as CPI


def principal_view(request):
    print("{0:.2f}".format(random.uniform(10.5,11.6)))
    return render(request,'testing/principalTesting.html',{'data':'data'})

def load_championships(request):
    CI.load_data()
    return redirect('test_principal')

def load_events(request):
    CPI.load_events()
    return redirect('test_principal')

def load_competitions(request):
    CPI.load_competitions()
    return redirect('test_principal')

def load_athletes(request):
    AI.load_athletes()
    return redirect('test_principal')

def delete_athletes(request):
    AI.delete_athletes()
    return redirect('test_principal')

def load_stages(request):
    CI.load_stages()
    return redirect('test_principal')

def generate_series(request):
    CPI.generate_series()
    return redirect('test_principal')

def delete_assignments(request):
    CPI.delete_assignments()
    return redirect('test_principal')