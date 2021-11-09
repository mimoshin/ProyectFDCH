from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from .models import *

#::::championship_signals::::
def new_champ(sender,instance,**kwargs):
    #print("NEW_CHAMP SIGNAL",kwargs)
    if kwargs['created']:
        stad = champ_stadistics.objects.all().last()
        stad.num_champs+=1
        stad.save()
        print("nuevo campeonato")
        #print("Incrementando campeonatos inscritos en 1")

def remove_champ(sender,instance,**kwargs):
    #print("REMOVE_CHAMP SIGNAL",kwargs)
    stad = champ_stadistics.objects.all().last()
    if stad.num_champs > 0 :
        stad.num_champs-=1
        stad.save()
    #print("Reduciendo campeonatos inscritos en 1")

#:::::::::::::::::::::::::::

#::::stage_signals::::
def new_stage(sender,instance,**kwargs):
    #print("NEW_STAGE SIGNAL",kwargs)
    if kwargs['created']:
        obj = instance.champ_fk 
        obj.number_stages +=1
        obj.save()

def remove_stage(sender,instance,**kwargs):
    #print("REMOVE_STAGE SIGNAL",kwargs)
    obj = instance.champ_fk 
    if obj.number_stages > 0: 
        obj.number_stages -=1
        obj.save()

#:::::::::::::::::::::

#::::competition_signals::::
def new_competition(sender,instance,**kwargs):
    #print("NEW_COMPETITION SIGNAL",kwargs)
    if kwargs['created']:
        obj = instance.stage_fk
        obj.num_compt +=1
        obj.save()

def remove_competition(sender,instance,**kwargs):
    #print("REMOVE_COMPETITION SIGNAL",kwargs)
    obj = instance.stage_fk
    if obj.num_compt > 0:
        obj.num_compt -=1
        obj.save()

#:::::::::::::::::::::

#::::inscription_signals::::
def new_inscription(sender,instance,**kwargs):
    #print("NEW_INSCRIPTION SIGNAL",kwargs)
    if kwargs['created']:
        obj = instance.compt_fk
        obj.num_inscriptions +=1
        obj.save()

def remove_inscription(sender,instance,**kwargs):
    #print("REMOVE_INSCRIPTION SIGNAL",kwargs)
    obj = instance.compt_fk
    if obj.num_inscriptions > 0:
        obj.num_inscriptions -=1
        obj.save()

#:::::::::::::::::::::::::::