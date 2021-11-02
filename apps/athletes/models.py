from django.db import models
from django.db.models.base import Model
from base.const import GENDER_CHOICES
#-------------MODELS---------------------------------------
class club(models.Model):
    #CLUB MODEL
    pass

class categories(models.Model):
    #CATEGORIES MODEL
    pass

class athletes(models.Model):
    #ATHLETE MODEL
    athleteName = models.CharField(max_length=200,null=False,blank=False,default='Nombre')
    athleteSurname = models.CharField(max_length=200,null=False,blank=False,default='Apellido')
    dni = models.CharField(max_length=200,null=False,blank=False,default='0.0.0-0')
    gender = models.IntegerField(choices=GENDER_CHOICES,null=False,blank=False,default=1)

    def name(self):
        return self.athleteName
    def surname(self):
        return self.athleteSurname
    def assign(self):
        assigns = self.relatedAthle.all()
        if len(assigns) == 0:
            return True
        else:
            return False
#----------------------------------------------------------