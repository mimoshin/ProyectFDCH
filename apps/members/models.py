from django.db import models
from django.db.models.base import Model
from .load import load_2

DICT = ['A','B','C','D','E','F','G','H','J','K','L','M','N',
              'O','P','Q','R','S','T','U','V','W','X','Y','Z']


# Create your models here.
"""
Perfiles Asociaciones
country -> Paises de participacion
region -> Regiones del pais 
club -> Clubes inscritos
admin_region -> Asociacion Regional
"""

class country(models.Model):
    # ID 
    # Nombre del pais
    pass

class region(models.Model):
    # ID
    # Pais (FK)
    # Nombre de la region
    pass

class asociation(models.Model):
    # ID
    # Región (FK)
    # Nombre de asociacion
    # Otro dato
    pass

class club(models.Model):
    # ID
    # Asocacion (FK)
    # Nombre del club
    pass

class athlete(models.Model):
    #ID
    # Primer | Segundo Nombre
    # Primer | Segundo Apellido
    # Sexo 
    # Edad
    # Fecha de nacimiento
    # ¿Region (FK) ?
    # Club (FK) 
    # Otro dato
    first_name = models.CharField(max_length=20,default='primer_nombre')
    second_name = models.CharField(max_length=20,default='segundo_nombre')
    flast_name = models.CharField(max_length=20,default='primer_apellido')
    slast_name = models.CharField(max_length=20,default='segundo_apellido')
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=20, default='genero')
    birth = models.CharField(max_length=20, default='fecha_nacimiento')
    rut = models.CharField(max_length=20, default='11.111.111-1')
    club = models.CharField(max_length=20, default='club')
    size = models.CharField(max_length=20, default='M')
    #height = models.DecimalField(max_digits=5, decimal_places=2, default=('1.75'))
    def __str__(self):
        return '%s %s | %s %s' % (self.first_name, self.second_name, self.flast_name, self.slast_name)

class Members_Interface():
    @staticmethod
    def get_function():
        pass
    @staticmethod
    def set_function():
        pass


class athlete_interface():
    @staticmethod
    def get_all_athletes():
        athletes = athlete.objects.all()
        return athletes
    @staticmethod
    def get_filter(data):
        try:
            athletes = athlete.objects.filter(first_name__icontains = data['name'])
            return athletes
        except Exception as e:
            print(e)
    
    @staticmethod
    def load_data():
        data = load_2()
        try:
            for x in data:
                if x[4] =='FEMENINO':
                    new = athlete(first_name=x[0], second_name=x[1], flast_name=x[2], slast_name=x[3], gender=x[4])
                    new.save()
        except Exception as e:
            print(e)
    
        