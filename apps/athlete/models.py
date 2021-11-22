from datetime import datetime
from django.db import models
from django.utils.dateparse import parse_date
from base.const import GENDER_CHOICES,CATEGORY_CHOICES, SEX_CHOICES
from member.models import Clubs

class fileslif(models.Model):
    archivo = models.CharField(max_length=200)
    texto = models.CharField(max_length=100000)

class Athletes(models.Model):
    clubId = models.ForeignKey(Clubs,null=False,blank=False,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200, default='FIRSTNAME')
    secondName = models.CharField(max_length=200,default='SECONNAME')
    surname =  models.CharField(max_length=200,default='SURNAME')
    secondSurname = models.CharField(max_length=200,default='sSURNAME')
    rut = models.CharField(max_length=200,default='RUT')
    gender = models.IntegerField(choices=GENDER_CHOICES,null=False,blank=False,default=0)
    birthdate = models.DateField(default='2021-07-25')
    age = models.IntegerField(default=0)
    categoria = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=0)
    size = models.CharField(max_length=4, null=False,blank=False,default='.')
    height = models.CharField(max_length=4,null=False,blank=False,default='.')
    cellphone = models.CharField(max_length=9,null=False,blank=False,default='.')
    email = models.CharField(max_length=30,null=False,blank=False,default='.')
    coach = models.CharField(max_length=10,null=False,blank=False,default='.')
    region = models.CharField(max_length=10,null=False,blank=False,default='.')
    created_at = models.DateTimeField(auto_now=True,null=False,blank=False)
    updated_at = models.DateTimeField(auto_now=True,null=False,blank=False)

    def __str__(self):
        return "%s %s" %(self.firstName,self.id)

    def name(self):
        return self.firstName

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
        if 35 > diference  and diference > 22 :
            return 7
        elif diference >=35:
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
    
    def assign(self):
        md,sp,jp,th = self.midassignments.all(),self.speedassignments.all(),self.jumpassignments.all(),self.throwassignments.all()
        counter = len(md)+len(sp)+len(jp)+len(th)
        if counter == 0:
            return True
        else:
            return False

    def get_gender(self):
        return SEX_CHOICES[self.gender][1]
        
class AthleteInterface():
    @staticmethod
    def get_all_athletes():
        athletes_list = Athletes.objects.all()
        return athletes_list
    
    @staticmethod
    def get_athletes_club(clID):
        athletes_list = Athletes.objects.filter(clubId_id=clID)
        return athletes_list
        
    @staticmethod
    def get_athletes(data):
        if data['name']:
            try:
                if data['category']:
                    print("implementar categorias")   
                athletes = Athletes.objects.filter(firstName__icontains=data['name'])
                return athletes
            except Exception as e:
                print("error en la busqueda de atletas",e)
        else:
            try:
                athletes = Athletes.objects.all()
                return athletes
            except Exception as e:
                print("error en la busqueda de atletas",e)
    
    @staticmethod
    def get_athlete(aid):
        atleta = Athletes.objects.get(id=aid)
        return atleta

    @staticmethod
    def new_athlete(data):
        """

                        clubId  
                        firstName  secondName  surname  secondSurname  
                        rut  gender  birthdate  age  
                        categoria (autocompletado)
                        size  height  cellphone email coach region 
        """
        try:
            pbirthdate = parse_date(data['birthdate'])
            # birthdate gender rut clubAthle secondSurname surname secondName firstName

            Athletes.objects.create(rut=data['rut'],firstName=data['firstName'],secondName=data['secondName'],
                                surname=data['surname'],secondSurname=data['secondSurname'],gender=data['gender'], birthdate=pbirthdate,
                                clubId_id=data['clubAthle'])
        except Exception as e:
            for a in data:
                print(a,type(a))
            print("Error al cargar atletas:",e,"|",data)