import pytz, datetime
from django.db import models
from django.utils.dateparse import parse_date
from championship.models import championship, stage, competition, inscription, serie_2
from members.models import athlete, club
from .Read_JSON import json_to_list

def str_to_DateTimeField(time):
    stgo_tz = pytz.timezone('America/Santiago') 
    aux = time.split(' ')
    a_date, a_time = aux[0].split('-'), aux[1].split(':')
    year,month,day = int(a_date[0]), int(a_date[1]), int(a_date[2])
    hour,minute,second =int(a_time[0]), int(a_time[1]), int(a_time[2]) 
    datetime_field = datetime.datetime(year,month,day,hour,minute,second,tzinfo=stgo_tz)
    return datetime_field



def determinate_format(time):
    """
    Determinar el formato de tiempo para lograr un standar
    opciones 
        Minutos
        -> 10:20'31 | 10:20:31 | 10:20"31 | 10.20.31
        Segundos
        -> 10.21 | 10'21 | 10"21 | 10:21
    ****DETERMINAR REGEX PARA EL RECONOCIMIENTO DE FORMATO****
    """
    #TOTAL DE RESGISTROS TRACK_RESULT 13.497
    aux = time.split(':')
    if len(aux) == 1:
        aux=time.split('.')
    return 1

def compare_times(time_one,time_two):
    one_time = {'minute':None,'second':None,'milisecond':None}
    second_time = {'minute':None,'second':None,'milisecond':None}
    format_one = [determinate_format(time_one),determinate_format(time_two)]
    #print('comparando markas',time_one,time_two)

def buble_sort_mark(inscriptions):
    large_list = len(inscriptions)
    for in_dex in range(large_list):
        aux=inscriptions[in_dex]
        for on_dex in range(large_list):
            second_aux = inscriptions[on_dex]
            compare_times(aux.mark,second_aux.mark)


def organizer_club(compt_id):
    total_ins = inscription.objects.filter(compt_fk_id=compt_id)
    data_clubs ={}
    print(len(total_ins))
    for x in total_ins:
        if data_clubs:
            club = x.otro.club_fk
            if data_clubs.get(club.id):
                data_clubs[club.id].append(x)
            else:
                data_clubs[club.id] = []
                data_clubs[club.id].append(x)
        else:
            club = x.otro.club_fk
            data_clubs[club.id] = []
            data_clubs[club.id].append(x)

    for data in data_clubs:
        #print('Total del club %s -> %s'%(data,len(data_clubs[data])))
        if len(data_clubs[data]) >5:
            buble_sort_mark(data_clubs[data])
        
    aux =  json_to_list('5000_RESULTS.json')
    aux_2 =  json_to_list('10000_RESULTS.json')
    print("Total de resultados:",len(aux)+len(aux_2))
    """  
    #for a in data_clubs:
    #    print('KEY:',a)
    #    for b in data_clubs[a]:
    #        print(b)
    """

# Create your models here.
#::::Championships_test:::::
class new_serie(models.Model):
    # ID	COMPETENCIA	NUM_SERIE VIENTO
    competition_fk = models.ForeignKey(competition,null=False, blank=False, on_delete=models.CASCADE)
    num_serie = models.IntegerField(default=1)
    wind = models.CharField(max_length=6, default='00.00')

class asignation(models.Model):
    # ID	SERIE	ATLETA	PISTA	MARCA	RESULTADO
    serie_fk = models.ForeignKey(new_serie, null=False, blank=False, on_delete=models.CASCADE)
    athlete_fk = models.CharField(max_length=30)
    pist = models.IntegerField(default=1)
    mark = models.CharField(max_length=20, default='99.99py')
    result = models.CharField(max_length=20, default='00.00')


#:::::::::::::::::::::::::::
class test_inscription_interface():
    @staticmethod
    def new_inscription(id_compt,id_athle):
        """
            Funcion para realizar inscripcion de un atleta a una competencia|prueba
            1- Consulta si ya fue hecha la inscripcion solicitada
            2.1- Si fue hecha retorna (BUSCAR QUE RETORNA)
            2.2- Si no fue hecha, realiza la inscripcion
            3- Si falla se noticia el errors
        """
        try:
            Query_inscription = inscription.objects.get(compt_fk_id=id_compt,otro_id=id_athle)
        except inscription.DoesNotExist:
            inscription.objects.create(compt_fk_id=id_compt,otro_id=id_athle)
        except Exception as e:
            print("****Test_inscription_interface**** \n",e)
    @staticmethod
    def rm_total_inscriptions(id_compt):
        Query_inscription = inscription.objects.filter(compt_fk_id=id_compt)
        for i in Query_inscription:
            i.delete()
    
class test_athlete_interface():
    @staticmethod
    def get_athletes_filter(local_gender,local_category):
        """
            Funcion para buscar atletas segun el filtro categoria y genero
            1- Busca todos los atletas por genero y categoria
            1.1- Si encuentra atletas con esas caracteristicas retorna la lista correspondiente 
            1.2- Si falla notifica el error
        """
        genders = {'DAMAS':1,'VARONES':2}
        aux_gender = genders[local_gender]
        try:
            athlete_list = athlete.objects.filter(categoria=local_category, gender=aux_gender)
            return athlete_list
        except Exception as e:
            print("****Test_athlete_interface****\n",e)
            return []
    
    @staticmethod
    def load_all_athletes(data_list):
        for in_dex in data_list:
            #print(in_dex['id'],in_dex['names'],in_dex['surnames'],in_dex['birthdate'],in_dex['club_id'])
            try:
                birthdate = parse_date(in_dex['birthdate'])
                athlete.objects.create( id=in_dex['id'], 
                                    first_name=in_dex['names'],
                                    flast_name=in_dex['surnames'],
                                    gender=in_dex['sex_id'], 
                                    birth=birthdate,
                                    rut=in_dex['rut'],
                                    club_fk_id=in_dex['club_id'])
                # first_name | second_name | flast_name | slast_name | age | gender | birth | rut | club_fk | size | categoria
            except Exception as e:
                print("ERROR",e,in_dex['birthdate'],in_dex['id'])

class test_competition_interface():
    @staticmethod
    def competition_inscription_partial(id_compt,amount):
        """
            Funcion para inscribir una cantidad de atletas a una competencia|prueba
            1- Busca los datos de la competencia|prueba
            2- Busca atletas optimos para la inscripcion
        """
        try:
            compt = competition.objects.get(id=id_compt)
            print("verificar limitaciones de la competencia")
            print(compt.description())
            limit_at,limit_cl = compt.get_limits()
            athlete_list = test_athlete_interface.get_athletes_filter(compt.gender,compt.categorys)
            if amount == 'AL':
                print('realizar todas las inscripciones')
                for index in athlete_list:
                    athlete = index
                    test_inscription_interface.new_inscription(compt.id,athlete.id)
            else:
                for index in range(int(amount)):
                    athlete = athlete_list[index]
                    test_inscription_interface.new_inscription(compt.id,athlete.id)
            organizer_club(compt.id)
        except competition.DoesNotExist as e:
            print("Competencia no encontrada",e)
        except Exception as e:
            print("****Test_competition_interface****\n",e)
        
    @staticmethod
    def get_series(id_compt):
        series_list = serie_2.objects.filter(competition_fk_id=id_compt)
        return series_list
    
    @staticmethod
    def remove_series(id_compt):
        Query_series = serie_2.objects.filter(competition_fk_id=id_compt)
        for x in Query_series:
            x.delete()

    @staticmethod
    def new_club(data):
        club.objects.create(id=data['id'],club_name=data['name'],asociation=data['region_id'])
    
    @staticmethod
    def load_all_clubs(data_list):
        for in_dex in data_list:
            club.objects.create(id=in_dex['id'],club_name=in_dex['name'],asociation=in_dex['region_id'])

class test_championship_interface():
    @staticmethod
    def load_championships():
        file_champ = json_to_list('championship.json')
        try:
            for in_dex in file_champ:
                init_time = str_to_DateTimeField(in_dex['initdate'])
                finish_time = str_to_DateTimeField(in_dex['findate'])
                championship.objects.create(id=in_dex['id'], event_name=in_dex['name'], init_date=init_time,
                                            finish_date=finish_time,direction=in_dex['address'])
        except Exception as e:
            print("ERROR AL CARGAR CAMPEONATO->",e)
        """
        id | name | initdate | findate | idRegion | address | created_at | updated_at
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
    @staticmethod
    def load_stages():
        file_stages = json_to_list('stages.json')
        try:
            for in_dex in file_stages:
                if in_dex['fecha'] == None:
                    in_dex['fecha'] = in_dex['created_at'][:10]
                stage.objects.create(id=in_dex['id'],date=in_dex['fecha'],stage_name=in_dex['name'],
                                     champ_fk_id=in_dex['championship_id'])
        except Exception as e:
            print("ERROR AL CARGAR ETAPAS->",e)
        """
        id | fecha | name | championship_id | created_at | updated_at 
        stage_name = models.CharField(max_length=30, default='NOMBRE_ETAPA')
        champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE)
        date = models.DateField(default='2021-12-12')
        init_hour = models.TimeField(default='08:00:00')
        finish_hour = models.TimeField(default='00:00:00')
        creator = models.CharField(max_length=30, default='ADMIN')
        num_compt = models.IntegerField(default=0)
        stage_num = models.IntegerField(default=1)
        """