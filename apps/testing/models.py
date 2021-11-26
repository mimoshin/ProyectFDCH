from django.utils.dateparse import parse_date
from athlete.models import Athletes
from championship.models import*
from competition.models import*
from member.models import*
from base.utils import str_to_DateTimeField
from .utils import loadPersonalBest
from championship.models import ChampionshipFactory as CHF


class championshipInterface():
    @staticmethod
    def load_championships(file):
        """
            championshipName = CharField(default='CAMPEONATO')
            startDate = DateTimeField(default=timezone.now)
            finishDate = DateTimeField(default=timezone.now)
            region = CharField(default='REGION')
            country = CharField(default='PAIS')
            address = CharField(default='DIRECCION')
            numberStages = IntegerField(default=0)
            category = CharField(default='000001000')    
            limitClubs = IntegerField(LIMIT_CLUB_CHOICES,default=0)
            limitAthletes = IntegerField(LIMIT_ATHLETE_CHOICES,default=0)
        """
        for data in file:
            try:
                data['initdate'] =  str_to_DateTimeField(data['initdate'])
                data['findate'] = str_to_DateTimeField(data['findate'])
                data['created_at'] = str_to_DateTimeField(data['created_at'])
                data['updated_at'] = str_to_DateTimeField(data['updated_at'])
        
                Championships.objects.create(id=data['id'],championshipName=data['name'],startDate=data['initdate'],
                    finishDate=data['findate'],region=data['idRegion'],address=data['address'],created_at=data['created_at'],
                    updated_at=data['updated_at'])
            except Exception as e:
                pass
                #print("Error al cargar atletas:",e)

    @staticmethod
    def delete_championships():
        allchamps = Championships.objects.all()
        for x in allchamps:
            try:
                x.delete()
            except:
                pass
    
    @staticmethod
    def load_stages(file):
        """ 
            championshipId = models.ForeignKey(Championships,null=False,blank=False,on_delete=models.CASCADE)
            stageName = models.CharField(max_length=200,null=False,blank=False,default='ETAPA')
            date = models.DateTimeField(null=False,blank=False,default=timezone.now)
            starHour = models.TimeField(blank=False,null=False,default='08:00:00')
            finishHour = models.TimeField(blank=False,null=False,default='18:00:00')
            adminId = models.CharField(max_length=200,null=False,blank=False,default='ADMINISTRADOR')
            numCompetitions = models.IntegerField(default=0)
            numStage = models.IntegerField(default=0)
        """
        for data in file:
            try:
                if data['fecha'] == None:
                    data['fecha'] = "1111-01-01"
                    
                data['fecha'] = parse_date(data['fecha'])
                data['created_at'] = str_to_DateTimeField(data['created_at'])
                data['updated_at'] = str_to_DateTimeField(data['updated_at'])
                Stages.objects.create(id=data['id'],championshipId_id=data['championship_id'],stageName=data['name'],
                    date=data['fecha'],created_at=data['created_at'],updated_at=data['updated_at'])
            except Exception as e:
                pass
                #print("error al cargar etapas",e)
            
    @staticmethod
    def delete_stages():
        stageslist = Stages.objects.all()
        for x in stageslist:
            x.delete()
    
    @staticmethod
    def load_clubs(file):
        for data in file:
            try:
                Clubs.objects.create(id=data['id'],clubName=data['name'])
            except Exception as e:
                pass
                #print("error al cargar clubes",e,data['id'])

    @staticmethod
    def delete_clubs():
        listclubs = Clubs.objects.all()
        for x in listclubs:
            x.delete()
        

class competitionInterface():
    @staticmethod
    def generate_inscriptions(comptID,num):
        compt = Competitions.objects.get(id=comptID)
        athles_list = Athletes.objects.filter(gender=compt.gender)
        ready = 0
        print(compt,len(athles_list))

        for athlete in athles_list:
            if ready == int(num):
                break
            else:
                Q = Inscriptions.objects.filter(competitionId_id=compt.id,athleteId_id=athlete.id).exists()
                if not Q:
                    Inscriptions.objects.create(competitionId_id=compt.id,athleteId_id=athlete.id)
                    ready+=1

        print("ready termino en ",ready)
        return "Generar inscripcion de %s atletas en la competencia %s"%(num,comptID)
        
    @staticmethod
    def remove_inscriptions(args):
        if args['option'] == 'all':
            compID = args['cID']
            insc_list = Inscriptions.objects.filter(competitionId_id=compID)
            for x in insc_list:
                x.delete()
            return "Eliminadas todas las inscripciones"

        elif args['option'] == 'only':
            insID = args['id']
            inscription = Inscriptions.objects.filter(id=insID)
            inscription.delete()
            return "Eliminada la inscripcion"
        return "E"

    @staticmethod
    def load_events(file):
        for data in file:
            try:
                Events.objects.create(id=data['id'],eventName=data['name'],eventType=data['type'])
            except Exception as e:
                pass
                #print("Error al cargar eventos: ",e,data['id'])
            
    @staticmethod
    def delete_events():
        eventlist = Events.objects.all()
        for x in eventlist:
            x.delete()

    @staticmethod
    def load_competitions(file):
        """
            eventId = models.ForeignKey(Events,null=False,blank=False,on_delete=models.CASCADE)
            stageId = models.ForeignKey(Stages,null=False,blank=False,on_delete=models.CASCADE)
            round = models.IntegerField(choices=ROUND_CHOICES,null=False,blank=False,default=0)
            hour = models.TimeField(null=False,blank=False,default='08:00:00')
            category = models.IntegerField(null=False,blank=False,default=0)
            gender = models.IntegerField(choices=GENDER_CHOICES,null=False,blank=False,default=0)
            combinated= models.IntegerField(choices=COMBINATED_CHOICES,null=False,blank=False,default=0) 
        "id" : 1,
		"hour" : "09:00:00",
		"sport_id" : 5,
		"category_id" : 4,
		"sex_id" : 1,
		"stage_id" : 1,
		"created_at" : "2018-05-26 02:11:01",
		"updated_at" : "2018-05-26 02:11:01",
		"competition_type_id" : 1   
        """
        for data in file:
            try:
                Competitions.objects.create(id=data['id'],eventId_id=data['sport_id'],stageId_id=data['stage_id'],
                    hour=data['hour'],gender=data['sex_id'])
            except Exception as e:
                pass
                #print("Error al cargar competencias:",e)

    @staticmethod 
    def delete_competition():
        allCompts = Competitions.objects.all()
        for x in allCompts:
            x.delete()

    @staticmethod
    def delete_assignments():
        lista = [SpeedHeats.objects.all(),MidHeats.objects.all(),JumpHeats.objects.all(),ThrowHeats.objects.all()]
        for x in lista:
            for a in x:
                a.delete()

    @staticmethod
    def generate_series():
        #tipo de serie
        heatClass = {1:SpeedHeats,2:MidHeats,3:JumpHeats,4:JumpHeats,5:ThrowHeats}
        #tipo de asignacion
        assingClass = {1:SpeedAssignments,2:MidAssignments,3:JumpAssignments,4:JumpAssignments,5:ThrowAssignments}
        comp_list = Competitions.objects.all()
        total_Athletes = Athletes.objects.all()

        #35 competencias, 8 x serie = 280
        for x in comp_list:
            """
                Seleccionar tipo de serie
                Filtrar atletas por genero
                Comprobar si los heats estan creadas | si no hay, se crean
            """
            selectedHeat = heatClass[x.get_type()]
            filter_athletes = total_Athletes.filter(gender=x.gender)

            try:
                data = x.get_relatedHeats()
                if len(data) == 0:
                    #print("Creando HEATS para %s"%(x.name()))
                    #selectedHeat.objects.create(competitionId_id=x.id,numberHeat=1)
                    for a in range(1,3):
                        selectedHeat.objects.create(competitionId_id=x.id,numberHeat=a)
                    data = x.get_relatedHeats()

                for heat in data:
                    #print("armando serie numero",heat.numberHeat)
                    selectedAssing = assingClass[x.get_type()]
                    index = 0
                    for atle in filter_athletes:
                        if index == 8:
                            #print("temine una serie",heat.numberHeat)
                            break
                        elif atle.assign():
                            PB = loadPersonalBest(x.eventId.id,x.get_type())
                            selectedAssing.objects.create(heatId_id=heat.id,athleteId_id=atle.id,personalBest=PB)
                            #print("objeto creado supuestamente")
                            index+=1
            except Exception as e:
                print("Error al generar series",e)  

    #_____SALTO LARGO Y TRIPLE_________________
    @staticmethod
    def load_jumpHeats(file):
        """
            "id" : 1,
		    "fecha_date" : null,
		    "hora" : null,
		    "sex_id" : 1,
		    "competition_id" : 9,
		    "sport_id" : 1,
		    "category_id" : 1,
		    "type" : null,
		    "created_at" : "2018-05-26 13:37:22",
		    "updated_at" : "2018-05-27 14:30:03",
		    "serie" : "Salto Largo - Hexatlón - Varones"

                competitionId = ForeignKey(Competitions)
                numberHeat = IntegerField(default=0)
                observation = CharField(default='S/0')
        """
        for data in file:
            try:
                JumpHeats.objects.create(id=data['id'],competitionId_id=data['competition_id'],observation=data['serie'])
            except Exception as e:
                pass
                #print("ERROR AL CARGAR JUMPHEATS",e)

    @staticmethod
    def delete_jumpHeats():
        heatlist = JumpHeats.objects.all()
        for x in heatlist:
            x.delete()
    
    @staticmethod
    def load_jumps(file):
        
        """
            "id" : 3,
		"jump_head2_id" : 1,
		"athlete" : "SANTIAGO SALINAS CABRERA",
		"club" : "A. SANTIAGO",
		"first" : "x",
		"vvfirst" : "+0.8",
		"second" : "5.25",
		"vvsecond" : "0.0",
		"third" : "5.22",
		"vvthird" : "-0.2",
		"op" : "",
		"fourth" : "",
		"vvfourth" : "",
		"fifth" : "",
		"vvfifth" : "",
		"sixth" : "",
		"vvsixth" : "",
		"achievement" : "5.25",
		"place" : "3",
		"created_at" : "2018-05-26 14:19:10",
		"updated_at" : "2018-05-27 13:13:18",
		"an" : "4/4/2003",
		"region" : "13",
		"points" : "431",
		"rut" : null,
		"bestAchievement" : null

                athleteId = ForeignKey(Athletes)
                personalBest = CharField(default='N/R')
                result = CharField(default=' ')
                place = IntegerField(default=0)
                strAthle = CharField(default=" ")
                strClub = CharField(default=" ")
                heatId = ForeignKey(JumpHeats)
   
        """
        for data in file:
            try:
                if data['athlete']:
                    if data['place'] == "DNS":
                        data['place'] = 0
    
                    elif not isinstance(data['place'],int):
                        data['place'] = 0

                    value = JumpHeats.objects.get(id=data['jump_head2_id']).competitionId.id
                    #Inscriptions.objects.create(athleteId_id=4144,strAthle=data['athlete'],competitionId_id=value)
                    ids = JumpAssignments.objects.create(id=data['id'],athleteId_id=4145,heatId_id=data['jump_head2_id'],strAthle=data['athlete'],strClub=data['club'],
                        place=data['place'])
                    try:
                        Inscriptions.objects.create(id=ids.id,athleteId_id=4145,strAthle=data['athlete'],competitionId_id=value)
                    except:
                        pass
            except Exception as e:
                pass
                #print("ERROR AL CARGAR JUMPS",e)

    @staticmethod
    def delete_jumps():
        asignlist = JumpAssignments.objects.all()
        for x in asignlist:
            x.delete()
    
    @staticmethod
    def load_jump_participations(file):
        """
            "id" : 3,
		    "first" : "x",
		    "vvfirst" : "+0.8",
		    "second" : "5.25",
		    "vvsecond" : "0.0",
		    "third" : "5.22",
		    "vvthird" : "-0.2",
		    "op" : "",
		    "fourth" : "",
		    "vvfourth" : "",
		    "fifth" : "",
		    "vvfifth" : "",
		    "sixth" : "",
		    "vvsixth" : "",
		    "achievement" : "5.25",
		    "place" : "3",
		    "points" : "431",
            assignmentId = ForeignKey(JumpAssignments)
            pNumber = IntegerField(default=0)
            result = CharField(default='X')
            wind = CharField(default='..')
        """
        participations =   [("first","vvfirst",1),("second","vvsecond",2), 
		                    ("third","vvthird",3),("fourth","vvfourth",4),
		                    ("fifth","vvfifth",5),("sixth","vvsixth",6)]
        for data in file:
            try:
                for p in participations:
                    result = data[p[0]]
                    wind = data[p[1]]
                    number = p[2]
                    if result == None:
                        result = ' '
                    if wind == None:
                        wind = ' '
                    JumpParticipation.objects.create(assignmentId_id=data['id'],pNumber=number,result=result,wind=wind)
            except Exception as e:
                print("ERROR AL CARGAR PARTICIPATION",e,data['id'])
                pass
    
    @staticmethod
    def delete_jump_participations():
        participationlist = JumpParticipation.objects.all()
        for x in participationlist:
            x.delete()
    #_____FIN SALTO LARGO Y TRIPLE_________________

    #______________SALTO ALTO Y CON GARROCHA__________________
    @staticmethod
    def load_HjumpHeats(file):
        """
                "id" : 1,
		        "fecha" : null,
		        "hora" : null,
		        "sex_id" : 1,
		        "competition_id" : 4,
		        "sport_id" : 1,
		        "category_id" : 1,
		        "serie" : "Salto Alto - Hexatlón - Damas",
		        "created_at" : "2018-05-26 13:24:25",
		        "updated_at" : "2018-05-26 15:26:45"

                competitionId = ForeignKey(Competitions)
                numberHeat = IntegerField(default=0)
                observation = CharField(default='S/0')
        """
        for data in file:
            try:
                hid = data['id']+1000
                JumpHeats.objects.create(id=hid,competitionId_id=data['competition_id'],observation=data['serie'])
            except Exception as e:
                pass
                #print("ERROR AL CARGAR JUMPHEATS",e)
    
    @staticmethod
    def load_Hjumps(file):
        """
                "id" : 10,
		        "hjump_head2_id" : 2,
		        "athlete" : "AGUSTINA CRUZ SEPÚLVEDA",
		        "an" : "3/31/2003",
		        "region" : "13",
		        "club" : "CDUC",
		        "achievement" : "DNS",
		        "place" : "99",
		        "created_at" : "2018-05-26 14:27:53",
		        "updated_at" : "2018-08-02 17:40:59",
		        "rut" : "212695041",
		        "bestAchievement" : null

                athleteId = ForeignKey(Athletes)
                personalBest = CharField(default='N/R')
                result = CharField(default=' ')
                place = IntegerField(default=0)
                strAthle = CharField(default=" ")
                strClub = CharField(default=" ")
                heatId = ForeignKey(JumpHeats)
   
        """
        pivot = Athletes.objects.get(firstName='PIVOTE')
        
        for data in file:
            try:
                if data['athlete']: 
                    place = data['place']
                if place == None or place == "" or len(place)>2 or place == 'FC' or place == '-':
                    data['place'] = 0
                if data['achievement'] == None:
                    data['achievement'] = " "
                hid= data['id']+10000
                headID = data['hjump_head2_id']+1000
                
                JumpAssignments.objects.create(id=hid,athleteId_id=pivot.id,heatId_id=headID,strAthle=data['athlete'],strClub=data['club'],
                    place=data['place'],result=data['achievement'])

            except Exception as e:
                print("Fallo ",data)
                #print("ERROR AL CARGAR HJUMPS",e,hid)
    #______________FIN SALTO ALTO Y CON GARROCHA__________________
    
    #______________PRUEBAS DE PISTA__________________
    @staticmethod
    def load_midHeats(file):
        try:
            pass
        except Exception as e:
            print("ERROR AL CARGAR JUMPHEATS",e)

    @staticmethod
    def delete_midHeats():
        heatlist = MidHeats.objects.all()
        for x in heatlist:
            x.delete()

    @staticmethod
    def load_mids(file):
        try:
            pass
        except Exception as e:
            print("ERROR AL CARGAR JUMPHEATS",e)

    @staticmethod
    def delete_mids():
        heatlist = MidHeats.objects.all()
        for x in heatlist:
            x.delete()

    @staticmethod
    def load_speedHeats(file):
        try:
            pass
        except Exception as e:
            print("ERROR AL CARGAR JUMPHEATS",e)

    @staticmethod
    def delete_speedpHeats():
        heatlist = SpeedHeats.objects.all()
        for x in heatlist:
            x.delete()
    @staticmethod
    def load_speeds(file):
        try:
            pass
        except Exception as e:
            print("ERROR AL CARGAR JUMPHEATS",e)

    @staticmethod
    def delete_speeds():
        heatlist = SpeedHeats.objects.all()
        for x in heatlist:
            x.delete()
#______________PRUEBAS DE PISTA__________________

#______________LANZAMIENTOS__________________
    @staticmethod
    def load_throwheats(file):
        for data in file:
            try:
                """
                    "id" : 1,
		            "fecha_date" : null,
		            "hora" : null,
		            "sex_id" : 1,
		            "competition_id" : 8,
		            "sport_id" : 1,
		            "category_id" : 1,
		            "type" : null,
		            "created_at" : "2018-05-26 13:35:10",
		            "updated_at" : "2018-05-27 14:29:28",   
		            "serie" : "Lanzamiento del Martillo - Final - Damas"

                competitionId = ForeignKey(Competitions)
                numberHeat = IntegerField(default=0)
                observation = CharField(default='S/0')
            """
                ThrowHeats.objects.create(id=data['id'],competitionId_id=data['competition_id'],observation=data['serie'])
        
            except Exception as e:
                print("ERROR AL CARGAR THROWHEATS",e)

    @staticmethod
    def delete_throwheats():   
        heatlist= ThrowHeats.objects.all()  
        for x in heatlist:
            x.delete() 

    @staticmethod
    def load_throws(file):
        """
                "id" : 2,
		        "throw_head2_id" : 1,
		        "athlete" : "CATALINA OBANDO NAHUELPAN",
		        "an" : "8/2/2004",
		        "club" : "C. D. BERNARDO FELMER",
		        "region" : "14",
		        "first" : "",
		        "second" : "",
		        "third" : "",
		        "op" : "",
		        "fourth" : "",
		        "fifth" : "",
		        "sixth" : "",
		        "achievement" : "N/M",
		        "place" : "",
		        "created_at" : "2018-05-26 14:02:24",
		        "updated_at" : "2018-05-26 19:44:29",
		        "bestAchievement" : null,
		        "rut" : null           

                athleteId = ForeignKey(Athletes)
                personalBest = CharField(default='N/R')
                result = CharField(default=' ')
                place = IntegerField(default=0)
                strAthle = CharField(default=" ")
                strClub = CharField(default=" ")
                heatId = ForeignKey(JumpHeats)
   
        """
        pivot = Athletes.objects.get(firstName='PIVOTE')
        for data in file:
            try:
                if data['athlete']:
                    if data['place'] == "DNS" or data['place'] == '':
                        data['place'] = 0
    
                    elif not isinstance(data['place'],int):
                        data['place'] = 0
                
                ThrowAssignments.objects.create(id=data['id'],athleteId_id=pivot.id,heatId_id=data['throw_head2_id'],strAthle=data['athlete'],strClub=data['club'],
                        place=data['place'])
            except Exception as e:
                print("ERROR AL CARGAR THROWS",e)
    @staticmethod
    def delete_throws():
        tlist = ThrowAssignments.objects.all()
        for x in tlist:
            x.delete()
    
    @staticmethod
    def load_throw_participations(file):
        """
                "id" : 2,
		        "throw_head2_id" : 1,
		        "athlete" : "CATALINA OBANDO NAHUELPAN",
		        "an" : "8/2/2004",
		        "club" : "C. D. BERNARDO FELMER",
		        "region" : "14",
		        "first" : "",
		        "second" : "",
		        "third" : "",
		        "op" : "",
		        "fourth" : "",
		        "fifth" : "",
		        "sixth" : "",
		        "achievement" : "N/M",
		        "place" : "",
		        "created_at" : "2018-05-26 14:02:24",
		        "updated_at" : "2018-05-26 19:44:29",
		        "bestAchievement" : null,
		        "rut" : null           

                athleteId = ForeignKey(Athletes)
                personalBest = CharField(default='N/R')
                result = CharField(default=' ')
                place = IntegerField(default=0)
                strAthle = CharField(default=" ")
                strClub = CharField(default=" ")
                heatId = ForeignKey(JumpHeats)
   
        """
        participations =   [("first",1),("second",2), 
		                    ("third",3),("fourth",4),
		                    ("fifth",5),("sixth",6)]

        for data in file:
            try:
                for p in participations:
                    result = data[p[0]]
                    number = p[1]
                    if result == None:
                        result = ' '
                    ThrowParticipation.objects.create(assignmentId_id=data['id'],pNumber=number,result=result)
            except Exception as e:
                print("ERROR AL CARGAR PARTICIPATIONs THROW",e,data['id'])

    @staticmethod
    def delete_throws_participations():
        tlist = ThrowParticipation.objects.all()
        for x in tlist:
            x.delete()
#________FIN LANZAMIENTOS________________

class memberInterface():
    @staticmethod
    def load_data():
        pass

    @staticmethod
    def delete_data():
        pass
    
class testingInterface():
    @staticmethod
    def get_competitions(champID):
        try:
            competition_list = Competitions.objects.filter(stageId__championshipId_id=champID)
            print(len(competition_list))
            return competition_list
            
        except Exception as e:
            print("error en get_competition",e)

    @staticmethod
    def get_inscriptions(compID):
        try:
            inscription_list = Inscriptions.objects.filter(competitionId_id=compID)
            return inscription_list
        except Exception as e:
            print("Error en get_inscriptions",e)
        
    @staticmethod
    def detectFile(name,json_file,option=False):
        CH = championshipInterface()
        CI = competitionInterface()
        AI = athleteInterface
        options = { 'championship.json':CHF.load_championship,'athletes.json':AI.load_athletes,
                    'clubs.json':CH.load_clubs,'stages.json':CH.load_stages,
                    'sports.json':CI.load_events,'competitions.json':CI.load_competitions,
                    'hjump2s.json':CI.load_Hjumps,'hjump_head2s.json':CI.load_HjumpHeats,
                    'jump2s.json':CI.load_jumps,'jump_head2s.json':CI.load_Hjumps}
        if options.get(str(name)):
            function = options[str(name)]
            function(json_file)



class athleteInterface():
    @staticmethod
    def load_athletes(file):
        """
            FUNCION MODIFICADA EN BASE AL ARCHIVO new_athletes.json
            id | rut
            firstname | secondname | thirdnames |fourname 
            fi_lastnames | se_lastnames | th_lastnames | fo_lastnames 
            sex_id | birthdate | cellPhone | mail | size | height 
            region_id | club_id
            created_at | updated_at 
        """
        for data in file:
            try:
                if data['idClub'] == None:
                    data['idClub'] = data['club_id']
                if data['idRegion'] == None:
                    data['idRegion'] = data['region_id']
                #Athletes.objects.create(clubId_id=data['idClub'],firstName=data['names'],surname=data['surnames'],
                                        #gender=data['sex_id'],rut=data['rut'])
                if data['id'] == 2966:
                    print("pillado")
                elif data['id'] == 4051:
                    print("pillado")
                else:
                    pbirthdate = parse_date(data['birthdate'])

                Athletes.objects.create(id=data['id'], rut=data['rut'],
                                    firstName=data['names'], surname=data['surnames'],                                    
                                    gender=data['sex_id'], birthdate=pbirthdate,
                                    cellphone=data['cellPhone'], email=data['mail'], size=data['size'], height=data['height'], 
                                    region=data['idRegion'], clubId_id=data['idClub'],
                                    created_at=data['created_at'], updated_at=data['updated_at'])
            except Exception as e:
                pass
                #print("Error al cargar atletas:",e,"|",data)

    @staticmethod
    def delete_athletes():
        atlist = Athletes.objects.all()
        for x in atlist:
            x.delete()