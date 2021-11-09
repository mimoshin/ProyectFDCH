from django.db import models
from django.db.models.base import Model

# Create your models here.
class champ_stadistics(models.Model):
    num_champs = models.IntegerField(default=0)

    def __str__(self):
        return "Campeonatos inscritos: %s" % (self.num_champs)

class athletes_stadistics(models.Model):
    num_athletes = models.IntegerField(default=0)

    def __str__(self):
        return "Atletas inscritos: %s" %(self.num_athletes)
    
