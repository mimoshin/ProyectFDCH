from os import stat
from django.contrib.auth.decorators import permission_required
from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from base.const import LIMIT_ATHLETE_CHOICES,LIMIT_CLUB_CHOICES, CATEGORY_CHOICES, STATUS_CHOICES
from base.utils import str_to_DateTimeField



class Championships(models.Model):
    # ID	NOMBRE_CAMPEONATO	FECHA_INICIO	FECHA_TERMINO	REGION	PAIS	DIRECCION   NUMERO_ETAPAS CATEGRIAS LIM_X_CLUB LIM_PRUEBAS
    # PK    event_name          init_date       finish_date     region  country direction   number_stages category  limit_club limit_athle
    championshipName = models.CharField(max_length=200, null=False,blank=False,default='CAMPEONATO') 
    startDate = models.DateTimeField(null=False,blank=False,default=timezone.now)
    finishDate = models.DateTimeField(null=False,blank=False,default=timezone.now)
    region = models.CharField(max_length=50,null=False,blank=False,default='REGION')
    country = models.CharField(max_length=50,null=False,blank=False,default='PAIS')
    address = models.CharField(max_length=50,null=False,blank=False,default='DIRECCION')
    numberStages = models.IntegerField(default=0)
    category = models.CharField(max_length=9,null=False,blank=False,default='000001000')    
    limitClubs = models.IntegerField(choices=LIMIT_CLUB_CHOICES,null=False,blank=False,default=0)
    limitAthletes = models.IntegerField(choices=LIMIT_ATHLETE_CHOICES,null=False,blank=False,default=0)
    status = models.IntegerField(choices=STATUS_CHOICES,null=False,blank=False,default=1)
    created_at = models.DateTimeField(null=False,blank=False,default=timezone.now)
    updated_at = models.DateTimeField(null=False,blank=False,default=timezone.now)

    def __str__(self):
        return "ID: %s | NOMBRE: %s"%(self.id,self.championshipName)

    def name(self):
        return self.championshipName.upper()

    def get_stages(self,**kwargs):
        return self.stages_set.all()

    def get_categorys(self):
        cat = ''
        for x in range(1,9): 
            if self.category[x] == '1':
                cat += CATEGORY_CHOICES[x][1]
                if x <9:
                    cat+=' '
        return cat

    def categorys_options(self):
        options = []
        for x in range(1,9): 
            if self.category[x] == '1':
                option = '<option value="'+str(x)+'">'+CATEGORY_CHOICES[x][1]+'</option>'
                options.append(option)
        return options
    
    def get_status(self):
        return STATUS_CHOICES[self.status][1]

    def not_status(self):
        if self.status == 1:
            self.status = 5
        elif self.status == 5:
            self.status = 1
        self.save()

class Stages(models.Model):
    championshipId = models.ForeignKey(Championships,null=False,blank=False,on_delete=models.CASCADE)
    stageName = models.CharField(max_length=200,null=False,blank=False,default='ETAPA')
    date = models.DateTimeField(null=False,blank=False,default=timezone.now)
    starHour = models.TimeField(blank=False,null=False,default='08:00:00')
    finishHour = models.TimeField(blank=False,null=False,default='18:00:00')
    adminId = models.CharField(max_length=200,null=False,blank=False,default='ADMINISTRADOR')
    numCompetitions = models.IntegerField(default=0)
    numStage = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES,null=False,blank=False,default=1)
    created_at = models.DateTimeField(null=False,blank=False,default=timezone.now)
    updated_at = models.DateTimeField(null=False,blank=False,default=timezone.now)
    
    def __str__(self):
        return "ID:%s | %s | %s"%(self.id,self.stageName,self.championshipId.championshipName)

    def name(self):
        return self.stageName.upper()

    def get_competitions(self):
        return self.competitions_set.all()
    
    def champ_name(self):
        return self.championshipId.championshipName
    
    def get_status(self):
        return STATUS_CHOICES[self.status][1]

    def not_status(self):
        if self.status == 1:
            self.status = 5
        elif self.status == 5:
            self.status = 1
        self.save()

class ChampionshipLogs(models.Model):
    pass

class StageLogs(models.Model):
    pass

class ChampionshipInterface():
    @staticmethod
    def get_all_championships():
        listchamp = Championships.objects.all()
        return listchamp

    @staticmethod
    def get_championship(cID):
        champ = Championships.objects.get(id=cID)
        return champ

    @staticmethod
    def get_allfor_championship(cID):
        champQ = Championships.objects.get(id=cID)
        stagesQ = champQ.stages_set.all()
        totalStages = []
        for data in stagesQ:
            competitionsQ = list(data.competitions_set.all().order_by('hour'))
            if len(competitionsQ) >0:
                compQ = {'stage':data,'competitions':competitionsQ}
            else:
                compQ = {'stage':data,'competitions':''}
            totalStages.append(compQ)
        return champQ,totalStages

    @staticmethod
    def create_championship(data):
        try:
            Championships.objects.create(championshipName=data['event_name'],startDate=data['init_date'],finishDate=data['finish_date'],
                                    region=data['region'],address=data['direction'],category=data['categorys'],
                                    limitClubs=data['limit_club'],limitAthletes=data['limit_athle'])
        except Exception as e:
            print("ERROR AL CREAR EL CAMPEONATO",e)

    @staticmethod
    def create_stage(data,cID):
        try:
            Stages.objects.create(championshipId_id=cID,stageName=data['stage_name'])
        except Exception as e:
            print("ERROR AL CREAR ETAPA",e)


class ChampionshipFactory():
    @staticmethod
    def load_championship(data_json):
        #Cargar campeonatos desde archivo json
        for data in data_json:
                try:
                    data['initdate'] =  str_to_DateTimeField(data['initdate'])
                    data['findate'] = str_to_DateTimeField(data['findate'])
                    data['created_at'] = str_to_DateTimeField(data['created_at'])
                    data['updated_at'] = str_to_DateTimeField(data['updated_at'])
        
                    Championships.objects.create(id=data['id'],championshipName=data['name'],startDate=data['initdate'],
                        finishDate=data['findate'],region=data['idRegion'],address=data['address'],created_at=data['created_at'],
                        updated_at=data['updated_at'])
                except Exception as e:
                    print("Error al cargar campeonato:",data['id'],e)

    @staticmethod
    def load_stages(data_json):
        #cargar etapas desde archivo json
        for data in data_json:
            try:
                if data['fecha'] == None:
                    data['fecha'] = "1111-01-01"
                    
                data['fecha'] = parse_date(data['fecha'])
                data['created_at'] = str_to_DateTimeField(data['created_at'])
                data['updated_at'] = str_to_DateTimeField(data['updated_at'])
                Stages.objects.create(id=data['id'],championshipId_id=data['championship_id'],stageName=data['name'],
                    date=data['fecha'],created_at=data['created_at'],updated_at=data['updated_at'])
            except Exception as e:
                print("error al cargar etapa",data.id,e)

    @staticmethod
    def load_data_json(filename,data_json):
        #Cargar los campeonatos o stages desde un archivo json
        if filename == 'championships.json':
            ChampionshipFactory.load_championship(data_json)
        elif filename == 'stages.json':
            ChampionshipFactory.load_stages(data_json)

    @staticmethod
    def delete_all_data(selected):
        #Eliminar todos los campeonatos o etapas
        option = {'championship':Championships,'stages':Stages}
        object_list = option[selected].objects.all()
        for aux in object_list:
            try:
                aux.delete()
            except Exception as e:
                print("Error al eliminar el %s: %s | %s "%(aux.id,e))

    @staticmethod
    def get_all_championships():
        champ_list = Championships.objects.all()
        return champ_list

    @staticmethod
    def get_championship(champID):
        champ = Championships.objects.get(id=champID)
        return champ

    @staticmethod
    def get_allfor_championship(champID):
        champQ = Championships.objects.get(id=champID)
        stagesQ = champQ.stages_set.all()
        totalStages = []
        for data in stagesQ:
            competitionsQ = list(data.competitions_set.all().order_by('hour'))
            if len(competitionsQ) >0:
                compQ = {'stage':data,'competitions':competitionsQ}
            else:
                compQ = {'stage':data,'competitions':''}
            totalStages.append(compQ)
        return champQ,totalStages

    @staticmethod
    def get_champ_and_stages(champID):
        champ = Championships.objects.get(id=champID)
        stages = champ.stages_set.all()
        return champ,stages
    @staticmethod
    def disable_stage(stageID):
        stage = Stages.objects.get(id=stageID)
        stage.not_status()

    @staticmethod
    def create_championship(data):
        try:
            Championships.objects.create(championshipName=data['event_name'],startDate=data['init_date'],finishDate=data['finish_date'],
                                    region=data['region'],address=data['direction'],category=data['categorys'],
                                    limitClubs=data['limit_club'],limitAthletes=data['limit_athle'])
        except Exception as e:
            print("ERROR AL CREAR EL CAMPEONATO",e)

    @staticmethod
    def create_stage(data,champID):
        try:
            print(data,champID)
            Stages.objects.create(championshipId_id=champID,stageName=data['stage_name'])
        except Exception as e:
            print("ERROR AL CREAR ETAPA",e)
        
    @staticmethod
    def modify_championship(champID,data):
        try:
            all_category =  ('SC','u16','u18','u20','u23','TD','CD','A','M')
            
        
            champ = Championships.objects.get(id=champID)
            categor = ''

            for x in all_category:
                if data.get(x):
                    data.pop(x)
                    categor +='1'
                else:
                    categor +='0'
            data['categorys'] = categor   
        
            if data['event_name']:
                champ.championshipName=data['event_name']
            if data['init_date']:
                champ.startDate=data['init_date']
            if data['finish_date']:
                champ.finishDate=data['finish_date']
            if data['region']:
                champ.region=data['region']
            if data['direction']:
                champ.address=data['direction']
            if data['categorys']:
                champ.category=categor 
            if data.get('atlexclub'):
                print("limitar atletas por club")
                champ.limitClubs=data['limit_club']
            if data['limit_athle']:
                champ.limitAthletes=data['limit_athle']
            champ.save()          
        except Exception as e:
            print("ERROR AL Modificar EL CAMPEONATO",e,data)