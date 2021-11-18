from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from base.const import LIMIT_ATHLETE_CHOICES,LIMIT_CLUB_CHOICES, CATEGORY_CHOICES



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

class Stages(models.Model):
    championshipId = models.ForeignKey(Championships,null=False,blank=False,on_delete=models.CASCADE)
    stageName = models.CharField(max_length=200,null=False,blank=False,default='ETAPA')
    date = models.DateTimeField(null=False,blank=False,default=timezone.now)
    starHour = models.TimeField(blank=False,null=False,default='08:00:00')
    finishHour = models.TimeField(blank=False,null=False,default='18:00:00')
    adminId = models.CharField(max_length=200,null=False,blank=False,default='ADMINISTRADOR')
    numCompetitions = models.IntegerField(default=0)
    numStage = models.IntegerField(default=0)
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