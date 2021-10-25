from os import execlpe
from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from members.models import athlete
from stadistics.models import champ_stadistics
from base.const import LIMIT_ATHLETE_CHOICES, LIMIT_CLUB_CHOICES, CATEGORY_CHOICES, SERIES_CHOICES, TEST_GROUP_CHOICES



class championship(models.Model):
    # ID	NOMBRE_CAMPEONATO	FECHA_INICIO	FECHA_TERMINO	REGION	PAIS	DIRECCION   NUMERO_ETAPAS CATEGRIAS LIM_X_CLUB LIM_PRUEBAS
    # PK    event_name          init_date       finish_date     region  country direction   number_stages category  limit_club limit_athle
    event_name = models.CharField(max_length=50, null=False, default='NOMBRE_CAMPEONATO') 
    init_date = models.DateTimeField(default=timezone.now, null=False)
    finish_date = models.DateTimeField(default=timezone.now, null=False)
    region = models.CharField(max_length=50, null=False, default='REGION')
    country = models.CharField(max_length=50, null=False, default='PAIS')
    direction = models.CharField(max_length=50, null=False, default='DIRECCION')
    number_stages = models.IntegerField(default=0)
    category = models.CharField(max_length=9,default='012345678')
    limit_club = models.IntegerField(choices=LIMIT_CLUB_CHOICES, default=0)
    limit_athle = models.IntegerField(choices=LIMIT_ATHLETE_CHOICES, default=0)

    """
    OPCIONALES:
    creator FK
    number_days = models.IntegerField(default=1)
    """

    def __str__(self):
        return "%s" % (self.event_name)

    def get_categorys(self):
        "Categorias incluidas en el campeonato"
        cate = ''
        for x in range(1,9): 
            if self.category[x] == '1':
                cate += CATEGORY_CHOICES[x][1]
                if x <9:
                    cate+=' '
        print("cargando categorias")
        return cate
    
    def categorys_options(self):
        options = []
        for x in range(1,9): 
            if self.category[x] == '1':
                option = '<option value="'+str(x)+'">'+CATEGORY_CHOICES[x][1]+' ('+CATEGORY_CHOICES[x][2]+')</option>'
                options.append(option)
        return options

    def get_categorys_count(self):
        num = 0 
        for x in range(1,9): 
            if self.category[x] == '1':
                num+=1
        return str(num)
                
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
   type_test = models.IntegerField(choices=TEST_GROUP_CHOICES, default=0)

   def get_type(self):
       return TEST_GROUP_CHOICES[int(self.type_test)][1]
   def __str__(self):
       return ("%s" % (self.test_name))


class competition(models.Model):
    # ID	ETAPA	PRUEBA	HORA	CATEGORIAS	GENERO
    stage_fk = models.ForeignKey(stage, null=False, blank=False, on_delete=models.CASCADE)
    test_fk = models.ForeignKey(test, null=False, blank=False, on_delete=models.CASCADE)
    round = models.IntegerField(choices=SERIES_CHOICES, blank=False, null=False, default=0)
    hour = models.TimeField(null=False, blank=False, default='08:00')
    categorys = models.IntegerField(default=1)
    gender = models.CharField(max_length=10, default='GENERO')
    series = models.BooleanField(default=False)
    num_series = models.IntegerField(default=0)
    num_inscriptions = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s | %s" % (self.test_fk.test_name, self.gender, self.hour, self.stage_fk) 
    
    def description(self):
        message = "Competencia %s \nRound: %s \nCategoria: %s \nGenero: %s " %(self.test_fk.test_name,self.round,self.get_category(),self.gender)
        return message

    def get_limits(self):
        champ = self.stage_fk.champ_fk
        #print('limite atletas por club %s | Limitar atletas por club y prueba %s' % (champ.limit_club,champ.limit_athle))
        return champ.limit_club,champ.limit_athle
    def get_category(self):
        return CATEGORY_CHOICES[self.categorys][1]
    def get_round(self):
        return SERIES_CHOICES[self.round][1]
    def str_cat(self):
        return str(self.categorys)
    def get_champ_compt(self):
        return "%s | %s | %s | %s" % (self.stage_fk.champ_fk ,self.test_fk, self.gender, self.get_category())

class inscription(models.Model):
    # ID	ATLETA	COMPETICION	MARCA
    otro = models.ForeignKey(athlete,null=False, blank=False, on_delete=models.CASCADE, default='1')
    athlete = models.CharField(max_length=10, default='ATLETA')
    compt_fk = models.ForeignKey(competition, null=False, blank=False, on_delete=models.CASCADE)
    mark = models.CharField(max_length=20, default='00.00.00')
    ready = models.BooleanField(default=False)

    def __str__(self):
        return "Atleta %s inscrito a %s" % (self.otro, self.compt_fk)
    def short_str(self):
        return '%s inscrito a %s '%(self.otro.first_name,self.compt_fk.test_fk.test_name)

class track_series(models.Model):
    # ID	INSCRIPCION	PISTA	NUM_SERIE	RESULTADO
    inscription = models.ForeignKey(inscription, null=False, blank=False, on_delete=models.CASCADE)
    pist = models.IntegerField(default=0)
    serie_num = models.IntegerField(default=0)
    result = models.CharField(max_length=20, default='hola')

class serie(models.Model):
    # ID Serie de prueba
    # Prueba | championship_activity (FK) 
    # Numero de serie
    # Velocidad del viento
    activity_fk = models.ForeignKey(competition, blank=False, null= False, on_delete=models.CASCADE)
    s_number = models.IntegerField(default=1)
    serie_type = models.CharField(max_length=20,default='Series')
    
    def __str__(self):
        return "Serie %s %s %s" % (self.s_number,self.activity_fk.test_fk,
                                   self.activity_fk.stage_fk)
class serie_2(models.Model):
    # ID	COMPETENCIA	NUM_SERIE VIENTO
    competition_fk = models.ForeignKey(competition,null=False, blank=False, on_delete=models.CASCADE)
    num_serie = models.IntegerField(default=1)
    wind = models.CharField(max_length=6, default='00.00')
    serie_type = models.IntegerField(choices=TEST_GROUP_CHOICES, default=0)

    def __str__(self):
        return "Serie %s - %s %s" %(self.num_serie,self.competition_fk.test_fk,self.competition_fk.gender)

class absAsignation(models.Model):
    serie_fk = models.ForeignKey(serie_2, null=False,blank=False, on_delete=models.CASCADE)
    athlete_fk = models.ForeignKey(athlete, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        abstract=True 

class trackAsignation(absAsignation):
    asign_type = models.CharField(max_length=20,default='1 POR PISTA')
    lane = models.IntegerField(default=0)
    mark = models.CharField(max_length=20, default='AUXILIAR')
    result = models.CharField(max_length=20, default='00')

class jumpAsignation(absAsignation):
    mark = models.CharField(max_length=20, default='AUXILIAR')
    total_results = models.CharField(max_length=200, default='first;second;third;fourth;five;six')
    total_winds = models.CharField(max_length=200, default='first;second;third;fourth;five;six')

class throwAsignation(absAsignation):
    mark = models.CharField(max_length=20, default='AUXILIAR')
    total_results = models.CharField(max_length=200, default='first;second;third;fourth;five;six')
    total_winds = models.CharField(max_length=200, default='first;second;third;fourth;five;six')

    def results_list(self):
        return self.total_results.split(';')

class asignation(models.Model):
    # ID	SERIE	ATLETA	PISTA	MARCA	RESULTADO
    serie_fk = models.ForeignKey(serie_2, null=False, blank=False, on_delete=models.CASCADE)
    athlete_fk = models.ForeignKey(athlete, null=False, blank=False, on_delete=models.CASCADE)
    pist = models.IntegerField(default=1)
    mark = models.CharField(max_length=20, default='99.99py')
    result = models.CharField(max_length=20, default='00.00')

    def __str__(self):
        return "%s inscrito a %s " % (self.athlete_fk,self.serie_fk)

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
        try:
            stad = champ_stadistics.objects.all().last()
            stad.num_champs+=1
            stad.save()
        except Exception as e:
            print("Signal Error to save championship")
        #print("Incrementando campeonatos inscritos en 1")

def remove_champ(sender,instance,**kwargs):
    print("REMOVE_CHAMP SIGNAL",kwargs['signal'])
    if kwargs.get('deleted'):
        try:
            stad = champ_stadistics.objects.all().last()
            if stad.num_champs > 0 :
                stad.num_champs-=1
                stad.save()
        except Exception as e:
            print("Signal Error to delete championship")
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
    @staticmethod
    def get_all_compt_for_champ():
        champ_list = championship.objects.all()
        competition_list = []
        for champ in champ_list:
            stages_list = champ.stage_set.all()
            for stage in stages_list:
                compts_list = stage.competition_set.all()
                for compt in compts_list:
                    print(compt)

    
    #__SET_FUNCTIONS__
    @staticmethod
    def create_championship(data):
        # event_name | init_date | finish_date | region | direction
        # direction | number_stages category | limit_club | limit_athle
        championship.objects.create(event_name=data['event_name'],init_date=data['init_date'],finish_date=data['finish_date'],
                                    region=data['region'],direction=data['direction'],category=data['categorys'],
                                    limit_club=data['limit_club'],limit_athle=data['limit_athle'])
    
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
    def get_all_competitions():
        competition_list = list(competition.objects.all())
        return competition_list

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
    def get_inscriptions_compt(ins_id):
        """
        Obtener todas las inscripciones de una competencia
        """
        try:
            inscriptions = inscription.objects.filter(compt_fk__id = ins_id)
            return inscriptions
        except Exception as e:
            print("STAGE_INTERFACE - Get inscription_compt ERROR",e)
    
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

    @staticmethod
    def get_competitions_filter(champ,cate,gend,atle):
        print(champ,"hola",cate,"hola2",gend,atle)
        try:
        
            gender_dict = {'2':'VARONES','1':'DAMAS'}
            compts = competition.objects.filter(stage_fk__champ_fk_id =champ,categorys=int(cate),gender=gender_dict[gend])
            html = '<tr>'
            print("hola",compts)
            for x in compts:
                html+= '<td>'+x.test_fk.__str__()+' '+x.gender+'</td>\
                        <td>'+x.get_category()+'</td>\
                        <td><input type="text" id="mark'+str(x.pk)+'" name="marka'+str(x.pk)+'"></td>\
                        <td> <div class="custom-control custom-switch">\
                                <input type="checkbox" class="custom-control-input" id="s'+str(x.pk)+'" name="COMPT-'+str(x.pk)+'" value="'+str(x.pk)+'">\
                                <label class="custom-control-label" for="s'+str(x.pk)+'"></label>\
                            </div>\
                        </td>'
                html+='</tr>'
            html+='<input type="hidden" name="athlete" id="athlete_inscription_pk" value="'+atle+'">'
            return html

        except Exception as e:
            print(e)

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
            competition.objects.create(stage_fk_id=stage_id, test_fk=act, hour=data_form['time'], 
                                       gender=data_form['gender'],categorys=data_form['category'],round=data_form['round'])
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
            test.objects.create(test_name=x+' METROS PLANOS', type_test=0)
        for x in hurdles:
            test.objects.create(test_name=x+' METROS VALLAS',type_test=0)
        for x in throw:
            test.objects.create(test_name=x,type_test=2)
        for x in jump:
            test.objects.create(test_name=x,type_test=1)



class competition_interface():
    @staticmethod
    def get_competition(id_compt):
        """
        Retorna la competencia requerida
        """
        compt = competition.objects.get(id=id_compt)
        return compt
        
class series_interface():
    @staticmethod
    def new_series(compt,amount):
        """
            ****Funcion para crear las series****
            1- Busca las inscripciones de la prueba
            2- Determina la cantidad de series a realizar
            3- Crea las series
            4- Asigna los atletas a cada serie
        """
        type_test = int(compt.test_fk.type_test)
        inscriptions_list = compt.inscription_set.filter(ready=False)
        other = list(compt.inscription_set.filter(ready=False))

        if compt.series:    
            print("ya fueron creadas las series")
        else:  
            num_series = int(inscriptions_list.count()/int(amount))
            print(num_series)
            for i_serie in range(num_series):
                
                try:
                    Q_serie = serie_2.objects.get(competition_fk_id=compt.id,num_serie=i_serie+1)
                    print("La Serie ya fue creada",Q_serie)
                except ObjectDoesNotExist as e:
                    new_serie = serie_2.objects.create(competition_fk_id=compt.id,num_serie=i_serie+1,wind='0.0')
                    counter = 0
                    while counter<8:
                        selected = other[0]
                        print("HOLA?")
                        if selected.ready == False:
                            if type_test == 0:
                                trackAsignation.objects.create(serie_fk_id=new_serie.id,athlete_fk_id=selected.otro.id)
                            elif type_test == 1:
                                jumpAsignation.objects.create(serie_fk_id=new_serie.id,athlete_fk_id=selected.otro.id)
                            elif type_test == 2:
                                throwAsignation.objects.create(serie_fk_id=new_serie.id,athlete_fk_id=selected.otro.id)
                            selected.ready=True
                            selected.save()
                        counter+=1
                        other.pop(0)
                    print("Serie Hecha: ",new_serie)
                except Exception as e:
                    print('Proceder a crear serie',e)
        compt.series = True
        compt.save()
                
    @staticmethod
    def get_series(compt_id):
        try:
            total_series =[]
            series_list = serie_2.objects.filter(competition_fk_id=compt_id)

            type_test = int(series_list[0].competition_fk.test_fk.type_test)
            for i_serie in series_list:
                if type_test == 0:
                    data =[i_serie,trackAsignation.objects.filter(serie_fk_id=i_serie.id)]

                elif type_test == 1:
                    data =[i_serie,jumpAsignation.objects.filter(serie_fk_id=i_serie.id)]
                elif type_test == 2:
                    data =[i_serie,throwAsignation.objects.filter(serie_fk_id=i_serie.id)]
                total_series.append(data)
            return total_series
        except Exception as e:
            print(e)