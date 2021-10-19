from types import MethodDescriptorType
from typing import Text
from django.db import models
from django.db.models import signals
from django.db.models.base import Model
from django.utils import timezone
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from members.models import athlete
from stadistics.models import champ_stadistics

class championship(models.Model):
    # ID	NOMBRE_CAMPEONATO	FECHA_INICIO	FECHA_TERMINO	REGION	PAIS	DIRECCION   NUMERO_ETAPAS
    # PK    event_name          init_date       finish_date     region  country direction   number_stages
    event_name = models.CharField(max_length=50, null=False, default='NOMBRE_CAMPEONATO') 
    init_date = models.DateTimeField(default=timezone.now, null=False)
    finish_date = models.DateTimeField(default=timezone.now, null=False)
    region = models.CharField(max_length=50, null=False, default='REGION')
    country = models.CharField(max_length=50, null=False, default='PAIS')
    direction = models.CharField(max_length=50, null=False, default='DIRECCION')
    number_stages = models.IntegerField(default=0)
    """
    OPCIONALES:
    creator FK
    category = models.IntegerField(default=1)
    stages = models.IntegerField(default=1) 
    number_days = models.IntegerField(default=1)
    """
    def __str__(self):
        return "%s" % (self.event_name)

class champ_log(models.Model):
    # ID	CAMPEONATO	FECHA	LOG	ADMIN
    champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE, default='1')
    date = models.DateField(default='2021-12-12', null=False)
    log = models.CharField(max_length=200, default='CAMBIO REALIZADO')
    admin = models.CharField(max_length=20, default='ADMIN') #LLAVE FORANEA ADMIN

class category(models.Model):
    # ID	NOMBRE_CATEGORIA	SIGLA_CATEGORIA
    category_name = models.CharField(max_length=10, null=False, default='CATEGORIA I')
    category_flag = models.CharField(max_length=10, null=False, default='GGWP')

class champ_category(models.Model):
    # Campeonato	Categoria
    champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE)
    categ_fk = models.ForeignKey(category, null=False, blank=False, on_delete=models.CASCADE)

class stage(models.Model):
    # ID	NOMBRE_ETAPA	CAMPEONATO	FECHA	HORA_INICIO	HORA_FIN    CREADOR     NUM_COMPT	ETAPA_NUM
    # PK    stage_name      champ_fk    date    init-hour   finish_hour creator     num_compt   stage_num
    stage_name = models.CharField(max_length=30, default='NOMBRE_ETAPA')
    champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(default='2021-12-12')
    init_hour = models.TimeField(default='08:00:00')
    finish_hour = models.TimeField(default='00:00:00')
    creator = models.CharField(max_length=30, default='ADMIN')
    num_compt = models.IntegerField(default=0)
    stage_num = models.IntegerField(default=1)

    def __str__(self):
        return "%s %s " % (self.stage_name, self.champ_fk)

class stage_log(models.Model):
    # ID	ETAPA	FECHA	LOG	ADMIN
    stage_fk = models.ForeignKey(stage, on_delete=models.CASCADE, null=False, blank=False, default='1')
    date = models.DateField(default='2021-12-12', null=False)
    log = models.CharField(max_length=20, default='CAMBIO REALIZADO')
    admin = models.CharField(max_length=20, default='ADMIN', null=False) #LLAVE FORANEA ADMIN

class test(models.Model):
   # ID	NOMBRE_PRUEBA TIPO
   test_name = models.CharField(max_length=20, null=False, default='PRUEBA X')
   type_test = models.CharField(max_length=20, null=False, default='TIPO X')
   
   def __str__(self):
        return "%s" % (self.test_name) 

class competition(models.Model):
    # ID	ETAPA	PRUEBA	HORA	CATEGORIAS	GENERO
    stage_fk = models.ForeignKey(stage, null=False, blank=False, on_delete=models.CASCADE)
    test_fk = models.ForeignKey(test, null=False, blank=False, on_delete=models.CASCADE)
    hour = models.TimeField(default='08:00', null=False, blank=False)
    categorys = models.IntegerField(default=11111)
    gender = models.CharField(max_length=10, default='GENERO')
    series = models.BooleanField(default=False)
    num_series = models.IntegerField(default=0)
    num_inscriptions = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s | %s" % (self.test_fk.test_name, self.gender, self.hour, self.stage_fk) 

class inscription(models.Model):
    # ID	ATLETA	COMPETICION	MARCA
    otro = models.ForeignKey(athlete,null=False, blank=False, on_delete=models.CASCADE, default='1')
    athlete = models.CharField(max_length=10, default='ATLETA')
    compt_fk = models.ForeignKey(competition, null=False, blank=False, on_delete=models.CASCADE)
    mark = models.CharField(max_length=20, default='00.00.00')

    def __str__(self):
        return "Atleta %s inscrito a %s" % (self.otro, self.compt_fk)

class track_series(models.Model):
    # ID	INSCRIPCION	PISTA	NUM_SERIE	RESULTADO
    inscription = models.ForeignKey(inscription, null=False, blank=False, on_delete=models.CASCADE)
    pist = models.IntegerField(default=0)
    serie_num = models.IntegerField(default=0)
    result = models.CharField(max_length=20, default=00.01)

class serie(models.Model):
    # ID Serie de prueba
    # Prueba | championship_activity (FK) 
    # Numero de serie
    # Velocidad del viento
    activity_fk = models.ForeignKey(competition, blank=False, null= False, on_delete=models.CASCADE)
    s_number = models.IntegerField(default=1)
    def __str__(self):
        return "Serie %s %s %s" % (self.s_number,self.activity_fk.activity_fk,
                                   self.activity_fk.stage_fk)

class second_serie(models.Model):
     # ID Serie de prueba
    # Prueba | championship_activity (FK) 
    # Numero de serie
    # Velocidad del viento
    activity_fk = models.ForeignKey(competition, blank=False, null= False, on_delete=models.CASCADE)
    s_number = models.IntegerField(default=1)
    wind = models.CharField(max_length=5)

    def __str__(self):
        return "Serie %s %s %s" % (self.s_number,self.activity_fk.activity_fk,
                                   self.activity_fk.stage_fk)

class track_inscription(models.Model):
    # ID
    # Atleta | athlete(FK)
    # Serie | serie (FK)
    # Resultado 
    # Marca inscripcion
    athlete_fk = models.CharField(max_length=30)
    serie_fk = models.ForeignKey(serie, blank=False, null= False, on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
    inscription_mark = models.CharField(max_length=20)

class second_track_inscription(models.Model):
    # ID
    # Atleta | athlete(FK)
    # Prueba-torneo | championship_activity(FK)
    # Resultado 
    # Marca inscripcion
    athlete_fk = models.CharField(max_length=30)
    ca_fk = models.ForeignKey(competition, blank=False, null= False, on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
    inscription_mark = models.CharField(max_length=20)

    def __str__(self):
        return "Atleta %s inscrito en %s" % (self.athlete_fk, self.ca_fk)

class field_inscription(models.Model):
    # ID
    # Serie | serie(FK)
    # Atleta | athlete(FK)
    # numero de intentos ¿?
    pass


#::::championship_signals::::
def new_champ(sender,instance,**kwargs):
    #print("NEW_CHAMP SIGNAL",kwargs)
    if kwargs['created']:
        stad = champ_stadistics.objects.all().last()
        stad.num_champs+=1
        stad.save()
        #print("Incrementando campeonatos inscritos en 1")

def remove_champ(sender,instance,**kwargs):
    #print("REMOVE_CHAMP SIGNAL",kwargs)
    stad = champ_stadistics.objects.all().last()
    if stad.num_champs > 0 :
        stad.num_champs-=1
        stad.save()
    #print("Reduciendo campeonatos inscritos en 1")
post_save.connect(new_champ,sender=championship)
post_delete.connect(remove_champ,sender=championship)
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

post_save.connect(new_stage,sender=stage)
post_delete.connect(remove_stage,sender=stage)
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

post_save.connect(new_competition,sender=competition)
post_delete.connect(remove_competition,sender=competition)
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

post_save.connect(new_inscription,sender=inscription)
post_delete.connect(remove_inscription,sender=inscription)
#:::::::::::::::::::::::::::

#:::Interfaces:::::::::
class Championship_Interface():
    # ID	NOMBRE_CAMPEONATO	FECHA_INICIO	FECHA_TERMINO	REGION	PAIS	DIRECCION   NUMERO_ETAPAS
    # PK    event_name          init_date       finish_date     region  country direction   number_stages
    #__GET_FUNCTIONS__
    @staticmethod
    def get_all_championships():
        champs_list = championship.objects.all()
        return champs_list
    @staticmethod
    def get_championship(c_id):
        champ = championship.objects.get(id=c_id)
        return champ
    @staticmethod
    def get_num_champs():
        aux = champ_stadistics.objects.all().last()
        return aux.num_champs
    #__SET_FUNCTIONS__
    @staticmethod
    def create_championship(data):
        # event_name | init_date | finish_date | region | country | direction 
        championship.objects.create(event_name=data['champ'],direction=data['direction'])
    
    @staticmethod
    def generator_champs(dict):
        if dict:
            championship.objects.create(event_name=dict[0],init_date=dict[1],finish_date=dict[2])

class stage_interface():
    # ID	NOMBRE_ETAPA	CAMPEONATO	FECHA	HORA_INICIO	HORA_FIN    CREADOR     NUM_COMPT	ETAPA_NUM
    # PK    stage_name      champ_fk    date    init-hour   finish_hour creator     num_compt   stage_num
    #__Get_functions__
    @staticmethod
    def get_stage(stage_id):
        local_stage = stage.objects.get(pk=stage_id)
        return local_stage
    @staticmethod
    def get_stage_comps(stage_id):
        competitions = list(competition.objects.filter(stage_fk__pk = stage_id))
        #print(competitions)
        return competitions
    @staticmethod
    def get_champ_stages(c_id):
        try:
            activitys = {}
            stage_list = stage.objects.filter(champ_fk__pk = c_id)
            for __stage__ in stage_list:
                if __stage__.num_compt > 0:
                    acts_list = stage_interface.get_stage_comps(__stage__.pk)
                    activitys[__stage__.pk] = acts_list
                else:
                    activitys[__stage__.pk] = None
            #print(activitys)
            return stage_list,activitys
        except Exception as e:
            print(e)
        return [],[]
    @staticmethod
    def get_champ_activitys(c_id):
        try:
            data = competition.objects.filter(stage_fk__champ_fk__pk = c_id)
            return data
        except Exception as e:
            print(e)

    @staticmethod
    def get_competition(c_id):
        try:
            compt = competition.objects.get(id = c_id)
            return compt
        except Exception as e:
            print(e)
    @staticmethod
    def get_inscriptions(ins_id):
        try:
            atletes = inscription.objects.filter(compt_fk__id = ins_id)
            return atletes
        except Exception as e:
            print(e)
    @staticmethod
    def get_complete_stages(champ):
        """
        1° Busca las etapas registradas, correspondientes a un campeonato
        2° Busca las competencias registradas en cada etapa 
        """
        competition_list = {}
        try:
            stages_list = champ.stage_set.all()
            for st_index in stages_list:
                compts = st_index.competition_set.all()
                if compts:
                    competition_list[st_index.pk] = compts
        except Exception as e:
            print(e)
            stages_list = []
        return stages_list, competition_list
    
    @staticmethod
    def get_championship_data(champ):
        """
        1° Busca las etapas registradas, correspondientes a un campeonato
        2° Busca las competencias registradas en cada etapa 
        """
        competition_list = {}
        try:
            stages_list = champ.stage_set.exclude(num_compt=0)
            for st_index in stages_list:
                compts = st_index.competition_set.all()
                if compts:
                    competition_list[st_index.pk] = compts
                    
        except Exception as e:
            print(e)
            stages_list = []
        return stages_list, competition_list


    #__SET_FUNCTIONS__
    @staticmethod
    def create_stage(data,c_id):
        #champ = Championship_Interface.get_championship(c_id)
        try:
            num = int(data['number_stage'])+1
            stage.objects.create(champ_fk_id=c_id, stage_name=data['stage_name'], stage_num=num)
        except Exception as e:
            print(e)

    @staticmethod
    def generator_stages(c_id,n_stage,name):
        try:
            stage.objects.create(champ_fk_id=c_id, stage_name=name, stage_num=n_stage)
        except Exception as e:
            print(e)
    @staticmethod
    def new_compt(stage_id,data_form):
        try:
            # stage (FK) | activity (FK) | star_hour | gender
            #print(data_form)
            #print(data_form['time'],data_form['compt'],data_form['round'],data_form['category'],data_form['gender'])
            #st_fk = stage.objects.get(pk=stage_id)
            #new_compt = competition(stage_fk=st_fk, test_fk=act, hour=data_form['time'], gender = data_form['gender'])
            #new_compt.save()
            act = test.objects.get(test_name=data_form['compt'])
            competition.objects.create(stage_fk_id=stage_id, test_fk=act, hour=data_form['time'], gender=data_form['gender'])
            return True
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def generator_compts(stage_id,test,gender):
        try:
            # stage (FK) | activity (FK) | star_hour | gender
            competition.objects.create(stage_fk_id=stage_id, test_fk=test,gender=gender)
            return True
        except Exception as e:
            print(e)
            
    @staticmethod
    def new_inscription(athle,compt):
        inscription.objects.create(otro_id=athle,compt_fk_id=compt)
        # ID	ATLETA	COMPETICION	MARCA
        # otro athlete compt_fk    mark
        """
        otro = models.ForeignKey(athlete,null=False, blank=False, on_delete=models.CASCADE, default='1')
        athlete = models.CharField(max_length=10, default='ATLETA')
        compt_fk = models.ForeignKey(competition, null=False, blank=False, on_delete=models.CASCADE)
        mark = models.CharField(max_length=20, default='00.00.00')
        """
        
            
class generator():
    @staticmethod
    def create_competitions():
        track = ['100','200','400','800','1500','5000','10000']
        hurdles = ['110','100','400']
        throw = ['LANZAMIENTO DE LA JABALINA', 'LANZAMIENTO DEL DISCO', 'LANZAMIENTO DE LA BALA']
        jump = ['SALTO ALTO', 'SALTO LARGO', 'SALTO TRIPLE']
        for x in track:
            test.objects.create(test_name=x+' METROS PLANOS')
        for x in hurdles:
            test.objects.create(test_name=x+' METROS VALLAS')
        for x in throw:
            test.objects.create(test_name=x)
        for x in jump:
            test.objects.create(test_name=x)

