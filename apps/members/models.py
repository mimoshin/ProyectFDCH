from django.db import models
from datetime import datetime
from django.db.models.fields import EmailField
from django.utils.dateparse import parse_date
from .load import load, load_2
from base.const import GENDER_CHOICES

DICT = ['A','B','C','D','E','F','G','H','J','K','L','M','N',
              'O','P','Q','R','S','T','U','V','W','X','Y','Z']

CATEGORY_CHOICES = ((0,'SIN CATEGORIA'),(1,'Sub 16'),
            (2,'Sub 18'),(3,'Sub 20'),
            (4,'Sub 23'),(5,'Todo Competidor'),
            (6,'Capacidades diferentes'),(7,'Adulto'),
            (8,'Master'))


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
    # ID Asocacion (FK) Nombre del club
    asociation = models.CharField(max_length=20, default='RM')
    club_name = models.CharField(max_length=20, default='CLUB')

    def __str__(self):
        return "Club: %s | ID: %s | PK: %s" % (self.club_name,self.id,self.pk)
    

class athlete(models.Model):
    #ID  |Primer-Segundo Nombre |Sexo   |Edad   |Fecha de nacimiento    |Region |Club   |otroxs 
    rut = models.CharField(max_length=20, default='11.111.111-1')
    first_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    second_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    third_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    four_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    flast_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    slast_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    thlas_tname = models.CharField(max_length=200,null=True, blank=True, default='.')
    folast_name = models.CharField(max_length=200,null=True, blank=True, default='.')
    birthdate = models.DateField(default='2021-07-25')
    age = models.IntegerField(default=20)
    categoria = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=0)
    club_fk = models.ForeignKey(club, blank=False, null=False, on_delete=models.CASCADE, default=15)
    size = models.CharField(max_length=4, null=True, blank=True, default='.')
    height = models.CharField(max_length=4,null=True, blank=True, default='.')
    cellphone = models.CharField(max_length=9,null=True, blank=True, default='.')
    email = models.CharField(max_length=30,null=True, blank=True, default='.')
    coach = models.CharField(max_length=10,null=True, blank=True, default='.')
    region = models.CharField(max_length=10,null=True, blank=True, default='.')
    created_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    
    def __str__(self):
        return '%s %s | %s %s' % (self.first_name, self.second_name, self.flast_name, self.slast_name)

    def get_category(self):
        return CATEGORY_CHOICES[self.categoria][1]

    def determinate_category(self):
        """
            *****************************************
            **--------------CATEGORIAS-------------** 
            *****************************************
            **  M = Master                    8    **
            **  A = Adulto                    7    **
            **  CD = Capacidades Diferentes   6    **
            **  TD = Todo competidor (TORNEO) 5    **
            **  u23 = Sub 23 (20-21-22)       4    **
            **  u20 = sub 20 (18-19)          3    **
            **  u18 = sub 18 (16-17)          2    **
            **  u16 = sub 16 (14-15)          1    **
            **  SC = Sin categria             0    **
            *****************************************
        """
        year = datetime.now()
        diference = year.year - self.birthdate.year
        if diference > 22:
            return 7
        elif diference >35:
            return 8
        elif diference < 14:
            return 0 
        else:
            try:
                category = {0:0,14:1,15:1,16:2,17:2,18:3,19:3,20:4,21:4,22:4}
                return category[diference]
            except Exception as e:
                print(e, self.birthdate,diference)

    def save(self,*args,**kwargs):
        self.categoria = self.determinate_category()
        return super().save(*args,**kwargs)

class Members_Interface():
    @staticmethod
    def get_function():
        pass
    @staticmethod
    def set_function():
        pass


class athlete_interface():
    @staticmethod
    def get_athletes_for_compt(compt):
        """
        Funcion para Test
        Retorna la cantidad de atletas que se pueden inscribir a una prueba
        """
        genders = {'None':0,'DAMAS':1,'VARONES':2,'MIXTO':3}
        gend = genders[compt.gender]
        athlete_count = athlete.objects.filter(categoria= compt.categorys, gender=gend).count()
        return athlete_count

    @staticmethod
    def get_all_athletes():
        athletes = athlete.objects.all()
        return athletes

    @staticmethod
    def get_filter(data):
        try:
            if data['name']:
                athletes = athlete.objects.filter(first_name__icontains=data['name'])
            else:
                athletes = athlete.objects.all()
            return athletes[:100]
        except Exception as e:
            print("ERROR AL OBTENER ATLETAS FILTRADOS",e)
    
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
    
    @staticmethod
    def new_load_athletes():
        data = load_2()
        #birth = models.DateField(default='11-11-2021')
        try:
            for x in data:
                uno = parse_date('2006-12-12')
                dos = parse_date('2004-12-12')
                tres = parse_date('2002-12-12')
                cuatro = parse_date('2000-12-12')
                cinco = parse_date('1996-12-12')
                new_uno = athlete(first_name=x[0], second_name=x[1], flast_name=x[2], slast_name=x[3], gender=x[4],birth=uno)
                new_uno.save()
                new_dos = athlete(first_name=x[0], second_name=x[1], flast_name=x[2], slast_name=x[3], gender=x[4],birth=dos)
                new_dos.save()
                new_tres = athlete(first_name=x[0], second_name=x[1], flast_name=x[2], slast_name=x[3], gender=x[4],birth=tres)
                new_tres.save()
                new_cuatro = athlete(first_name=x[0], second_name=x[1], flast_name=x[2], slast_name=x[3], gender=x[4],birth=cuatro)
                new_cuatro.save()
                new_cinco = athlete(first_name=x[0], second_name=x[1], flast_name=x[2], slast_name=x[3], gender=x[4],birth=cinco)
                new_cinco.save()
                
        except Exception as e:
            print('error',e)
    
    @staticmethod
    def delete_all_athletes():
        list_a = athlete.objects.all()
        for x in list_a:
            x.delete()
