from django.db import models
from athletes.models import athletes
from championships.models import stages
from base.const import GENDER_CHOICES, EVENT_TYPE_CHOICES, ROUND_CHOICES


#-------------COMPETITION & EVENTS ------------------------

class events(models.Model):
    eventName = models.CharField(max_length=200,null=False,blank=False,default='EVENTO ..')
    eventType = models.IntegerField(choices=EVENT_TYPE_CHOICES,null=False,blank=False,default=1)

    def __str__(self):
        return "ID: %s | Prueba: %s"%(self.id,self.eventName)
    def name(self):
        return self.eventName

class competitions(models.Model):
    eventId = models.ForeignKey(events,null=False,blank=False,on_delete=models.CASCADE)
    stageId = models.ForeignKey(stages,null=False,blank=False,on_delete=models.CASCADE)
    round = models.IntegerField(choices=ROUND_CHOICES,null=False,blank=False,default=1)
    initDate = models.CharField(max_length=200,null=False,blank=False,default='08:00')
    gender = models.IntegerField(choices=GENDER_CHOICES,null=False,blank=False,default=0)
    comb= models.CharField(max_length=200,null=False,blank=False,default='NO')

    def __str__(self):
        gender = GENDER_CHOICES[self.gender][1]
        return "ID: %s |Etapa: %s | Evento: %s %s"%(self.id,self.stageId.name(),self.eventId.name(),gender)
    def get_gender(self):
        return GENDER_CHOICES[self.gender][1]
    def name(self):
        return "%s %s"%(self.eventId.name(),self.get_gender())
    def type(self):
        return self.eventId.eventType
    def file(self):
        #AGREGAR FIELD ROUND PARA DETERMINAR SI SON SERIES, FINAL, ETC
        return "%s SERIES.xlsx"%(self.name())
    def get_round(self):
        return ROUND_CHOICES[self.round][1]
    def get_relatedHeats(self):
        options = {1:self.speedheats.all,2:self.mdheats.all,3:self.jumpheats.all,4:self.jumpheats.all,5:self.throwheats.all}
        related_function = options[self.type()]
        return related_function()

    def combi(self):
        if self.comb == 'NO':
            return False
        else:
            return True
#----------------------------------------------------------

#-------------COMPETITION SERIES---------------------------
class asbtractHeats(models.Model):
    #ASBTACT MODEL 
    competitionId = models.ForeignKey(competitions,related_name="%(class)s",null=False,blank=False,on_delete=models.CASCADE)
    numberHeat = models.IntegerField()
    observation = models.CharField(max_length=200,default='S/O')
    class Meta:
        abstract = True

class mdHeats(asbtractHeats):
    #SERIES DE MEDIOFONDO
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Serie %s"%(self.numberHeat)

class speedHeats(asbtractHeats):
    #SERIES DE VELOCIDAD
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Serie %s"%(self.numberHeat)

class jumpHeats(asbtractHeats):
    #SERIES DE SALTO
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Serie %s"%(self.numberHeat)

class throwHeats(asbtractHeats):
    #SERIES DE LANZAMIENTO
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Serie %s"%(self.numberHeat)
#----------------------------------------------------------


#-------------EVENT ASSIGNMENTS----------------------------
class abstractAssignments(models.Model):
    #ASBTRACT MODEL 
    athleteId = models.ForeignKey(athletes,related_name='relatedAthle',null=False,blank=False,on_delete=models.CASCADE)
    personalBest = models.CharField(max_length=200,default='NPB')
    result = models.CharField(max_length=200,default='NR')
    place = models.IntegerField(default=0)
   
class mdAssignments(abstractAssignments):
    #ASIGNACIONES MEDIOFONDO
    heatId = models.ForeignKey(mdHeats,related_name='asign',null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()
class speedAssignments(abstractAssignments):
    #ASIGNACIONES VELOCIDAD
    heatId = models.ForeignKey(speedHeats,related_name='asign',null=False,blank=False,on_delete=models.CASCADE)
    line = models.IntegerField(default=0)
    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()

class jumpAssignments(abstractAssignments):
    #ASIGNACIONES DE SALTO
    heatId = models.ForeignKey(jumpHeats,related_name='asign',null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()

class throwAssignments(abstractAssignments):
    #ASIGNACIONES DE LANZAMIENTO
    heatId = models.ForeignKey(throwHeats,related_name='asign',null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()
#----------------------------------------------------------

#-------------PARTICIPATIONS-------------------------------
class asbtractParticipations(models.Model):
    #ABSTRACT MODEL
    pass

class jumpParticipation(asbtractParticipations):
    #INTENTO DE SALTO
    pass

class throw(asbtractParticipations):
    #INTENTO DE LANZAMIENTO
    pass
#----------------------------------------------------------


#-------------COMBINATED EVENTS----------------------------
class asbtractPoints(models.Model):
    #ASBTRACT MODEL
    pass

class mdPoints(asbtractPoints):
    #PUNTAJE EN MEDIOFONDO
    pass

class speedPoints(asbtractPoints):
    #PUNTAJE EN VELOCIDAD
    pass

class jumpPoints(asbtractPoints):
    #PUNTAJE EN SALTO
    pass

class throwPoints(asbtractPoints):
    #PUNTAJE EN LANZAMIENTO
    pass

#----------------------------------------------------------

class competitionInterface():
    @staticmethod
    def get_competition(id):
        competition = competitions.objects.get(id=id)
        return competition
    
    @staticmethod
    def get_heats(cid,Type):
        heats = {1:speedHeats,2:mdHeats,3:jumpHeats,5:throwHeats}
        try:
            heat_class = heats[Type]
            heats_list = list(heat_class.objects.filter(competitionId=cid))
            total_data = []
            for data in heats_list:
                aux_dict = {'heat':data,'assign':list(data.asign.all())}
                total_data.append(aux_dict)
            return total_data
        except Exception as e:
            print("error buscando los heats",e)

