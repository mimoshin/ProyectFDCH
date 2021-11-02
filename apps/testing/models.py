import random
from athletes.models import*
from championships.models import*
from competitions.models import*
from members.models import*
from .Read_JSON import json_to_list
from .utils import loadPersonalBest


class athleteInterface():
    @staticmethod
    def load_athletes():
        jslist = json_to_list('athletes.json')
        try:
            for data in jslist:
                athletes.objects.create(athleteName=data['names'],athleteSurname=data['surnames'],
                                        gender=data['sex_id'],dni=data['rut'])
        except Exception as e:
            print("Error al cargar atletas:",e)

    @staticmethod
    def delete_athletes():
        atlist = athletes.objects.all()
        for x in atlist:
            x.delete()

class championshipInterface():
    @staticmethod
    def load_data():
        jslist = json_to_list('championship.json')
        try:
            for data in jslist:
                championships.objects.create(id=data['id'],championshipName=data['name'])
        except Exception as e:
            print("Error al cargar atletas:",e)

    @staticmethod
    def delete_data():
        atlist = athletes.objects.all()
        for x in atlist:
            x.delete()
    
    @staticmethod
    def load_stages():
        try:
            stages.objects.create(id=1,champId_id=86,stageName="Etapa 1 (Mañana)")
            stages.objects.create(id=2,champId_id=86,stageName="Etapa 2 (Tarde)")
            stages.objects.create(id=3,champId_id=86,stageName="Etapa 3 (Mañana)")
            stages.objects.create(id=4,champId_id=86,stageName="Etapa 4 (Tarde)")
        except Exception as e:
            print("error al cargar etapas",e)
        
class competitionInterface():
    @staticmethod
    def load_events():
        jslist = json_to_list('generalSports.json')
        try:
            for data in jslist:
                events.objects.create(id=data['id'],eventName=data['name'],eventType=data['type'])
        except Exception as e:
            print("Error al cargar eventos: ",e)

    def load_competitions():
        jslist = json_to_list('generalCompetitions.json')
        try:
            for data in jslist:
                competitions.objects.create(id=data['id'],eventId_id=data['eventId'],stageId_id=data['stageId'],
                                            initDate=data['initDate'],gender=data['gender'])
        except Exception as e:
            print("Error al cargar competencias:",e)

    @staticmethod
    def delete_data():
        atlist = athletes.objects.all()
        for x in atlist:
            x.delete()
    
    @staticmethod
    def delete_assignments():
        lista = [speedHeats.objects.all(),mdHeats.objects.all(),jumpHeats.objects.all(),throwHeats.objects.all()]
        for x in lista:
            for a in x:
                a.delete()

    @staticmethod
    def generate_series():
        heatClass = {1:speedHeats,2:mdHeats,3:jumpHeats,4:jumpHeats,5:throwHeats}
        assingClass = {1:speedAssignments,2:mdAssignments,3:jumpAssignments,4:jumpAssignments,5:throwAssignments}
        comp_list = competitions.objects.all()
        total_Athletes = athletes.objects.all()
        for x in comp_list:
            selectedHeat = heatClass[x.type()]
            filter_athletes = total_Athletes.filter(gender=x.gender)
            try:
                data = x.get_relatedHeats()
                if len(data) == 0:
                    #print("Creando HEATS para %s"%(x.name()))
                    for a in range(1,5):
                        selectedHeat.objects.create(competitionId_id=x.id,numberHeat=a)
                    data = x.get_relatedHeats()

                for heat in data:
                    #print("armando serie numero",heat.numberHeat)
                    selectedAssing = assingClass[x.type()]
                    index = 0
                    while index<8:
                        for atle in filter_athletes:
                            if index == 8:
                                #print("temine una serie",heat.numberHeat)
                                break
                            elif atle.assign():
                                PB = loadPersonalBest(x.eventId.id,x.type())
                                selectedAssing.objects.create(heatId_id=heat.id,athleteId_id=atle.id,personalBest=PB)
                                #print("objeto creado supuestamente")
                                index+=1
            except Exception as e:
                print("Error al generar series",e)            

class memberInterface():
    @staticmethod
    def load_data():
        pass

    @staticmethod
    def delete_data():
        pass
    
class testingInterface():
    @staticmethod
    def dataGestion():
        pass

