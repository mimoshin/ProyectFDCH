from django.db import models
from develop.read_json import json_to_list
from others.models import sexes

# Create your models here.
class championship(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    initdate = models.CharField(max_length=200,null=True,blank=True)
    findate = models.CharField(max_length=200,null=True,blank=True)
    idRegion = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "nombre: %s region: %s "%(self.name,self.idRegion)

class stage(models.Model):
    fecha = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    championship_id = models.ForeignKey(championship, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "id: %s name: %s "%(self.id,self.name)

class registration_head2(models.Model):
    championship_id = models.ForeignKey(championship,on_delete=models.CASCADE,null=False,blank=False)
    sex_id = models.ForeignKey(sexes,on_delete=models.CASCADE,null=False,blank=False)
    fecha = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    lastname = models.CharField(max_length=200,null=True,blank=True)
    an = models.CharField(max_length=200,null=True,blank=True)
    club = models.CharField(max_length=200,null=True,blank=True)
    region = models.CharField(max_length=200,null=True,blank=True)
    pais = models.CharField(max_length=200,null=True,blank=True)
    dni = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class championshipInterface():
    
    @staticmethod
    def load_championships():
        """
        Funcion que carga los campeonatos almacenados en el archivo json.
        id | name | initdate | findate | idRegion | address | created_at | updated_at 
        """
        champ_list = json_to_list('championship.json')
        for in_dex in champ_list:
            try:
                championship.objects.create(id=in_dex['id'], name=in_dex['name'], initdate=in_dex['initdate'],
                                        findate=in_dex['findate'], idRegion=in_dex['idRegion'], address=in_dex['address'],
                                        created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar campeonato",e)
    
    @staticmethod
    def delete_championships():
        champ_list = championship.objects.all()
        for x in champ_list:
            x.delete()

    @staticmethod
    def load_stages():
        stage_list = json_to_list('stages.json')
        """
        Funcion que carga las etapas almacenados en el archivo json.
        id | fecha | name | championship_id | created_at | updated_at
        """
        for in_dex in stage_list:
            try:
                stage.objects.create(id=in_dex['id'],fecha=in_dex['fecha'], name=in_dex['name'],
                                     championship_id_id = in_dex['championship_id'],
                                     created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar stages",e)

    @staticmethod
    def delete_stages():
        stage_list = stage.objects.all()
        for x in stage_list:
            x.delete()
    
    @staticmethod
    def load_registrationheads():
        print("cargar registrations_Head")
        registration_list = "archivo retornado por json"

    @staticmethod
    def delete_registrationheads():
        registration_list = registration_head2.objects.all()
        for x in registration_list:
            x.delete()
    
    
    