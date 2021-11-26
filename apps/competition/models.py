from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import tree
from base.const import EVENT_TYPE_CHOICES,ROUND_CHOICES,GENDER_CHOICES,COMBINATED_CHOICES, CATEGORY_CHOICES, STATUS_CHOICES
from championship.models import Stages
from athlete.models import Athletes
from .utils import  orderTimesSpeed




#-------------COMPETITION & EVENTS ------------------------
class Events(models.Model):
    eventName = models.CharField(max_length=200,null=False,blank=False,default='Evento')
    eventType = models.IntegerField(choices=EVENT_TYPE_CHOICES,null=False,blank=False,default=0)

    def __str__(self):
        return "ID: %s | Prueba: %s"%(self.id,self.eventName)

    def name(self):
        return self.eventName

    def get_type(self):
        return EVENT_TYPE_CHOICES[self.eventType][1]


    ########Signals########
    #######################

class Competitions(models.Model):
    eventId = models.ForeignKey(Events,null=False,blank=False,on_delete=models.CASCADE)
    stageId = models.ForeignKey(Stages,null=False,blank=False,on_delete=models.CASCADE)
    round = models.IntegerField(choices=ROUND_CHOICES,null=False,blank=False,default=0)
    hour = models.TimeField(null=False,blank=False,default='08:00:00')
    category = models.IntegerField(null=False,blank=False,default=0)
    gender = models.IntegerField(choices=GENDER_CHOICES,null=False,blank=False,default=0)
    combinated= models.IntegerField(choices=COMBINATED_CHOICES,null=False,blank=False,default=0)
    series = models.BooleanField(null=False,blank=False,default=False)
    observation = models.CharField(max_length=200,null=True,blank=True,default='S/C')
    status = models.IntegerField(choices=STATUS_CHOICES,null=False,blank=False,default=1)

    def __str__(self):
        return "ID: %s %s %s %s "%(self.id,self.eventId.name(),self.get_gender(),self.stageId.champ_name())

    def name(self):
        return "%s %s"%(self.eventId.name(),self.get_gender())
    
    def description(self):
        if self.combinated == 0:
            return "%s %s "%(self.eventId.name(),self.get_gender())
        else:
            return "%s %s %s"%(self.eventId.name(),self.get_combinated(),self.get_gender())

    def get_CID(self):
        return self.stageId.championshipId.id
        
    def get_gender(self):
        return GENDER_CHOICES[self.gender][1]

    def get_type(self):
        return self.eventId.eventType

    def get_round(self):
        if self.round == 0:
            return ROUND_CHOICES[1][1]
        else:
            return ROUND_CHOICES[self.round][1]
        
    def get_relatedHeats(self):
        options = {1:self.speedheats.all,2:self.midheats.all,3:self.jumpheats.all,4:self.jumpheats.all,5:self.throwheats.all}
        related_function = options[self.get_type()]
        return related_function()

    def get_category(self):
        if self.category == 0:
            return CATEGORY_CHOICES[5][1]
        else:
            return CATEGORY_CHOICES[int(self.category)][1]

    def get_combinated(self):
        return COMBINATED_CHOICES[self.combinated][1]

    def get_inscriptions(self):
        total = self.inscriptions_set.all().count()
        return total
    
    def set_series(self,series=False):
        print("self.series", self.series)
        if self.series:
            self.series = False
        else:
            self.series = True
        self.save()

    ########Signals########
    #######################

class Inscriptions(models.Model):
    athleteId = models.ForeignKey(Athletes,null=False,blank=False,on_delete=models.CASCADE)
    competitionId = models.ForeignKey(Competitions,null=False,blank=False,on_delete=models.CASCADE)
    personalBest = models.CharField(max_length=200,null=False,blank=False,default='N/R')
    strAthle = models.CharField(max_length=200,null=False,blank=False,default='PIVOTE')
    strClub = models.CharField(max_length=200,null=False,blank=False,default='PIVOTE')

#----------------------------------------------------------

#-------------COMPETITION SERIES---------------------------
class AbstractHeats(models.Model):
    #ABSTRACT MODEL
    competitionId = models.ForeignKey(Competitions,related_name="%(class)s",null=False,blank=False,on_delete=models.CASCADE)
    numberHeat = models.IntegerField(null=False,blank=False,default=0)
    observation = models.CharField(max_length=200,default='S/0')
    class Meta:
        abstract=True
    def __str__(self):
        """asbtract __str__"""

class MidHeats(AbstractHeats):
    #SERIES DE MEDIOFONDO
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Serie %s"%(self.numberHeat)

class SpeedHeats(AbstractHeats):
    wind = models.CharField(max_length=4,default='N/R')
    #SERIES DE VELOCIDAD
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Serie %s"%(self.numberHeat)

class JumpHeats(AbstractHeats):
    #SERIES DE SALTO
    def __str__(self):
        return "%s SERIE %s %s"%(self.competitionId.name(),self.numberHeat, self.id)
    def serie(self):
        return "Grupo %s"%(self.numberHeat)

class ThrowHeats(AbstractHeats):
    #SERIES DE LANZAMIENTO
    def __str__(self):
        return "%s SERIE %s"%(self.competitionId.name(),self.numberHeat)
    def serie(self):
        return "Grupo %s"%(self.numberHeat)
#----------------------------------------------------------

#-------------EVENT ASSIGNMENTS----------------------------
class AbstractAssignments(models.Model):
    #ASBTRACT MODEL 
    athleteId = models.ForeignKey(Athletes,related_name="%(class)s",null=False,blank=False,on_delete=models.CASCADE)
    personalBest = models.CharField(max_length=200,default='N/R')
    result = models.CharField(max_length=200, default=' ')
    place = models.IntegerField(default=0)
    strAthle = models.CharField(max_length=200,null=False,blank=False,default="PIVOTE")
    strClub = models.CharField(max_length=200,null=False,blank=False,default="PIVOTE")

    class Meta:
        abstract=True
    def __str__(self):
        """asbtract __str__"""
    def get_place(self):
        if self.place == 0:
            return ' '
        else:
            return self.place

    def description(self):
        if self.athleteId.id == 4144:
            return self.strAthle
        else:
            return self.athleteId.name()
    
    def get_result(self):
        try:
            r = self.assigneds.all().order_by('result').last()
            if r:
                return r.result
            else:
                return '-'
        except Exception as e:
            print("ERROR AL EXTRAER EL RESULTADO",self.id,e)
            return 0
    ########Signals########
    #######################

class MidAssignments(AbstractAssignments):
    #ASIGNACIONES MEDIOFONDO
    heatId = models.ForeignKey(MidHeats,related_name='asigned',null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()

class SpeedAssignments(AbstractAssignments):
    #ASIGNACIONES VELOCIDAD
    heatId = models.ForeignKey(SpeedHeats,related_name='asigned',null=False,blank=False,on_delete=models.CASCADE)
    line = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)], default=0)

    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()

class JumpAssignments(AbstractAssignments):
    #ASIGNACIONES DE SALTO
    heatId = models.ForeignKey(JumpHeats,related_name='asigned',null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s TORNEO : %s "%(self.strAthle,self.heatId,self.heatId.competitionId.get_CID())
    def athlete(self):
        return self.athleteId.name()

    def my_participations(self):
        print("HOLA HOLA")
        lista = self.assigneds.all()
        print("asigneds",lista)
        return "hola"

    def render_participations(self):
        participations = self.assigneds.all()
        return participations

########Signals########
#@receiver(post_save,sender=JumpAssignments)
#def new_assignment(sender,instance,**kwargs):
#    if kwargs['created']:
#        try:
#           athle,club,cID = instance.strAthle,instance.strClub,instance.heatId.competitionId.id
#          Inscriptions.objects.create(athleteId_id=4144,strAthle=athle,strClub=club,competitionId_id=cID)
#     except Exception as e:
#        print("error en signal new_assignment",e)
            
@receiver(post_delete,sender=JumpAssignments)
def remove_assignmente(sender,instance,**kwargs):
    print(kwargs)
#######################

class ThrowAssignments(AbstractAssignments):
    #ASIGNACIONES DE LANZAMIENTO
    heatId = models.ForeignKey(ThrowHeats,related_name='asigned',null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s"%(self.athleteId.name(),self.heatId)
    def athlete(self):
        return self.athleteId.name()

#----------------------------------------------------------

#-------------PARTICIPATIONS-------------------------------
class AsbtractParticipations(models.Model):
    #ABSTRACT MODEL
    class Meta:
        abstract=True
    def __str__(self):
        return """asbtract __str__"""

class JumpParticipation(AsbtractParticipations):
    #INTENTO DE SALTO
    assignmentId = models.ForeignKey(JumpAssignments,related_name="assigneds",null=False,blank=False,on_delete=models.CASCADE)
    pNumber = models.IntegerField(null=False,blank=False,default=0)
    result = models.CharField(max_length=10,null=False,blank=False,default='X')
    wind = models.CharField(max_length=10,null=False,blank=False,default='..')

class ThrowParticipation(AsbtractParticipations):
    #INTENTO DE LANZAMIENTO
    assignmentId = models.ForeignKey(ThrowAssignments,related_name="assigneds",null=False,blank=False,on_delete=models.CASCADE)
    pNumber = models.IntegerField(null=False,blank=False,default=0)
    result = models.CharField(max_length=10,null=False,blank=False,default='X')
#----------------------------------------------------------


#-------------COMBINATED EVENTS----------------------------
class AsbtractPoints(models.Model):
    #ABSTRACT MODEL
    class Meta:
        abstract=True
    def __str__(self):
        return """asbtract __str__"""

class MidPoints(AsbtractPoints):
    #PUNTAJE EN MEDIOFONDO
    pass

class SpeedPoints(AsbtractPoints):
    #PUNTAJE EN VELOCIDAD
    pass

class JumpPoints(AsbtractPoints):
    #PUNTAJE EN SALTO
    pass

class ThrowPoints(AsbtractPoints):
    #PUNTAJE EN LANZAMIENTO
    pass
#----------------------------------------------------------

#------------------FACTORYS -------------------------------

class CompetitionFactory():
    @staticmethod
    def get_all_events():
        listevents = Events.objects.all()
        return listevents

    @staticmethod
    def get_event(eID):
        event = Events.objects.get(id=eID)
        return event

    @staticmethod
    def get_all_competitions():
        competition_list = Competitions.objects.all()
        return competition_list

    @staticmethod
    def get_competition(cID):
        try:
            competition_list = Competitions.objects.get(id=cID)
            return competition_list
        except Exception as e:
            print("error en get_competition",e)
    
    @staticmethod 
    def get_competitions_champ(champID):
        try:
            competition_list = Competitions.objects.filter(stageId__championshipId__id=champID).order_by('stageId','hour')
            return competition_list
        except Exception as e:
            print("error en get_competitions_champ",e)

    @staticmethod
    def get_inscriptions(cID):
        inslist = Inscriptions.objects.filter(competitionId=cID)
        return inslist
        
    @staticmethod
    def get_my_participations(asID):
        pass

    
    @staticmethod
    def get_heats(cID,htype):
        heats = {1:SpeedHeats,2:MidHeats,3:JumpHeats,5:ThrowHeats,4:JumpHeats}
        try:
            #tipo de competencia
            heat_class = heats[htype]
            heats_list = list(heat_class.objects.filter(competitionId=cID))
            total_data = []
            for data in heats_list:
                total = data.asigned.all().order_by('place')
                aux_dict = {'heat':data,'assign':list(total)}
                total_data.append(aux_dict)
            return total_data

        except Exception as e:
            print("error buscando los heats",e)
            
    @staticmethod
    def get_compt_for_atle(data):
        try:
            compts = Competitions.objects.filter(stageId__championshipId_id=data['champ'],gender=data['gender'])
            html = '<tr>'
            contador = 0
            for x in compts:
                html+= '<td>'+x.description()+' '+x.get_gender()+'</td>\
                        <td>category</td>\
                        <td><input type="text" id="mark'+str(x.id)+'" name="marka'+str(x.id)+'"></td>\
                        <td> <div class="custom-control custom-switch">\
                                <input type="checkbox" class="custom-control-input" id="s'+str(x.id)+'" name="COMPT-'+str(x.id)+'" value="'+str(x.pk)+'">\
                                <label class="custom-control-label" for="s'+str(x.id)+'"></label>\
                            </div>\
                        </td>'
                html+='</tr>'
                contador+=1
            html+='<input type="hidden" name="athlete" id="athlete_inscription_pk" value="'+str(data['atle'])+'">'
            #return html
            return compts

        except Exception as e:
            print(e)
    
    @staticmethod
    def get_jumps(asID):
        try:
            # assignmentId pNumber result wind
            asigned = JumpAssignments.objects.get(id=asID)
            if asigned.strAthle == 'PIVOTE':
                name = asigned.athleteId.name()
            else:
                name = asigned.strAthle
            listP = JumpParticipation.objects.filter(assignmentId_id=asID).order_by('pNumber')
            print(len(listP))
            if listP:
                html = '<tr>'
                for x in listP:
                    html+= '<td class="text-center">'+x.result+'</td>\
                            <td class="text-center">'+x.wind+'m/s</td>'
                html+='</tr>'
            else:
                html = '<td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>\
                            <td class="text-center">-</td>'
            return {'body':html,'name':name}
        except Exception as e:
            print("ERROR AL CARGAR SALTOS",e)
            return False

    @staticmethod
    def set():
        pass
    
    @staticmethod
    def generate_series(cID):
        comp = Competitions.objects.get(id=cID)
        inscriptions_list = list(Inscriptions.objects.filter(competitionId_id=cID))

        #tipo de serie
        heatClass = {1:SpeedHeats,2:MidHeats,3:JumpHeats,4:JumpHeats,5:ThrowHeats}
        selectedHeat = heatClass[comp.get_type()]
        #tipo de asignacion
        assingClass = {1:SpeedAssignments,2:MidAssignments,3:JumpAssignments,4:JumpAssignments,5:ThrowAssignments}
        selectedAssing = assingClass[comp.get_type()]

        """
            Seleccionar tipo de serie
            Filtrar atletas por genero
            Comprobar si los heats estan creadas | si no hay, se crean
            Calcular la cantidad de series y atletas por serie, por defecto son 8
        """
        try:
            tinsc = len(inscriptions_list)
            if comp.series:
                print("Series ya creadas")

            else:
                if tinsc > 0:
                    if comp.series:
                        relateds = comp.get_relatedHeats()
                        for x  in relateds:
                            x.delete()
                    else:
                        if tinsc > 8:
                            max_series = int(len(inscriptions_list)/8)
                            for a in range(max_series):
                                selectedHeat.objects.create(competitionId_id=comp.id,numberHeat=a+1)
                        else:
                            max_series = 1
                            selectedHeat.objects.create(competitionId_id=comp.id,numberHeat=1)

                            relateds = comp.get_relatedHeats()
                           
                            for heat in relateds:
                                print("x")
                                cont = 0
                                while cont <tinsc:
                                    insc = inscriptions_list[0]
                                    if cont == tinsc:
                                        break
                                    else:
                                        #PB = loadPersonalBest(comp.eventId.id,comp.get_type())
                                        selectedAssing.objects.create(heatId_id=heat.id,athleteId_id=insc.athleteId.id)
                                        cont+=1
                                        if tinsc>1:
                                            inscriptions_list = inscriptions_list[1:]
                                        else:
                                            break
                        comp.set_series(True)
        except Exception as e:
            print("Error al generar series",e)  


    @staticmethod
    def new_competition(stageID,data):
        try:
            #print("Hora: ",data['time'],"\nPrueba: ",data['compt'])
            #print("Ronda: ",data['round'],"\nCategoria ",data['category'])
            #print("Genero: ",data['gender'],"\nCombinada: ",data['comb'])
            Competitions.objects.create(stageId_id=stageID, eventId_id=data['compt'], hour=data['time'], 
                gender=data['gender'],category=data['category'],round=data['round'],combinated=data['comb'])
            return True
        except Exception as e:
            print(e)
            return False
 
    @staticmethod
    def new_inscription(athle,compt):
        Inscriptions.objects.create(athleteId_id=athle,competitionId_id=compt)
        # ID	ATLETA	COMPETICION	MARCA
        # otro athlete compt_fk    mark
    
    @staticmethod
    def new_event(data):
        Events.objects.create(eventName=data['eventName'],eventType=data['eventType'])

    @staticmethod
    def changeResult(cpt,at,value):
        #buscar atleta asignado con la serie x 
        assingClass = {1:[SpeedAssignments,orderTimesSpeed],2:[MidAssignments,orderTimesSpeed],
                        3:[JumpAssignments,orderTimesSpeed],4:[JumpAssignments,orderTimesSpeed],
                        5:[ThrowAssignments,orderTimesSpeed]}
        try:
            data = at.split('-')
            selectedClass = assingClass[cpt][0]
            selected = selectedClass.objects.get(athleteId_id=data[1],heatId_id=data[0])
            selected.result = value
            selected.save()
            total = selectedClass.objects.filter(heatId_id=data[0])
            assingClass[cpt][1](total)
            
            #for x in range(0,len(total)):
             #   total[x].place = x+1
              #  total[x].save()
        except Exception as e:
            print("error al cambiar el resultado",e)