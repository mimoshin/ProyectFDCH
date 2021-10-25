from develop.read_json import json_to_list
from os import stat
from django.db import models

# Create your models here.
from django.db import models

class sexes(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: %s name: %s "%(self.id,self.name)

class categories(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: %s name: %s "%(self.id,self.name)
    

class asbtractInterface():
    @staticmethod
    def load_categories():
        """
        id | name | created_at | updated_at 
        """
        json_list = json_to_list('categories.json')
        for in_dex in json_list:
            try:
                categories.objects.create(id=in_dex['id'], name=in_dex['name'],
                                        created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar categories",e)

    @staticmethod
    def delete_categories():
        categorie_list = categories.objects.all()
        for x in categorie_list:
            x.delete()

    @staticmethod
    def load_sexes():
        json_list = json_to_list('sexes.json')
        """
        id | name | created_at | updated_at 
        """
        for in_dex in json_list:
            try:
                sexes.objects.create(id=in_dex['id'], name=in_dex['name'],
                                        created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar sexes",e)
    
    @staticmethod
    def delete_sexes():
        sexes_list = sexes.objects.all()
        for x in sexes_list:
            x.delete()