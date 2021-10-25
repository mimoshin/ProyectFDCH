import json
from django.db import models
from django.db.models.base import Model
from championships.models import stage
from athletes.models import athlete
from athletes.utils import *
from develop.read_json import json_to_list
from others.models import categories,sexes

# Create your models here.
class sport(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "id: %s name: %s "%(self.id,self.name)

class competition(models.Model):
    hour = models.CharField(max_length=200,null=True,blank=True)
    sport_id = models.ForeignKey(sport, on_delete=models.CASCADE, null=False, blank=False)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE, null=False, blank=False)
    sex_id = models.ForeignKey(sexes, on_delete=models.CASCADE, null=False, blank=False)
    stage_id = models.ForeignKey(stage, on_delete=models.CASCADE, null=False, blank=False)
    competition_type_id = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: %s name: %s "%(self.id,self.sport_id)

class track_head2s(models.Model):
    fecha = models.CharField(max_length=200,null=True,blank=True)
    hora = models.CharField(max_length=200,null=True,blank=True)
    sport_id = models.ForeignKey(sport,  on_delete=models.CASCADE, null=False, blank=False, default=1)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE, null=False, blank=False, default=1)
    sex_id = models.ForeignKey(sexes, on_delete=models.CASCADE, null=False, blank=False, default=1)
    competition_id = models.ForeignKey(competition, on_delete=models.CASCADE, null=False, blank=False)
    wind = models.CharField(max_length=200,null=True,blank=True)
    serie = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: %s name: %s %s "%(self.id,self.competition_id, self.competition_id.category_id)

class track2s(models.Model):
    track_head2s_id = models.ForeignKey(track_head2s, on_delete=models.CASCADE, null=False, blank=False)
    place =  models.CharField(max_length=200,null=True,blank=True)
    achievement =  models.CharField(max_length=200,null=True,blank=True)
    athlete =  models.CharField(max_length=200,null=True,blank=True)
    an =  models.CharField(max_length=200,null=True,blank=True)
    club =  models.CharField(max_length=200,null=True,blank=True)
    region =  models.CharField(max_length=200,null=True,blank=True)
    pais =  models.CharField(max_length=200,null=True,blank=True)
    rail = models.CharField(max_length=200,null=True,blank=True)
    start = models.CharField(max_length=200,null=True,blank=True)
    bestAchievement = models.CharField(max_length=200,null=True,blank=True)
    rut = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ID_Track2s: %s | TH2: %s | Atleta: %s | lugar %s | marca %s"%(self.id,self.track_head2s_id.id,self.athlete,self.achievement, self.place)

class resume_track(models.Model):
    trackhead2s = models.ForeignKey(track_head2s,null=False,blank=False,on_delete=models.CASCADE)
    athlete = models.CharField(max_length=200,default='VACIO')

    def __str__(self):
        return "ID: %s | tch2: %s | athleta: %s"%(self.id,self.trackhead2s,self.athlete)

class resume_throw(models.Model):
    throwhead = models.CharField(max_length=200,default='VACIO')
    athlete = models.CharField(max_length=200,default='VACIO')

    def __str__(self):
        return "ID: %s | tch2: %s | athleta: %s"%(self.id,self.throwhead,self.athlete)
    
class resume_jump(models.Model):
    jumphead = models.CharField(max_length=200,default='VACIO')
    athlete = models.CharField(max_length=200,default='VACIO')

    def __str__(self):
        return "ID: %s | tch2: %s | athleta: %s"%(self.id,self.jumphead,self.athlete)

class resume_Hjump(models.Model):
    jumphead = models.CharField(max_length=200,default='VACIO')
    athlete = models.CharField(max_length=200,default='VACIO')

    def __str__(self):
        return "ID: %s | tch2: %s | athleta: %s"%(self.id,self.jumphead,self.athlete)

class competitionInterface():
    @staticmethod
    def load_competitions():
        """
        Funcion que carga las competencias almacenadas en el archivo json.
        id | hour | sport_id | category_id | sex_id | stage_id | competition_type_id | created_at | updated_at
        """
        compt_list = json_to_list('competitions.json')
        for in_dex in compt_list:
            try:
                competition.objects.create(id=in_dex['id'],hour=in_dex['hour'], sport_id_id=in_dex['sport_id'],
                                     category_id_id = in_dex['category_id'], sex_id_id=in_dex['sex_id'],
                                     stage_id_id=in_dex['stage_id'], competition_type_id=in_dex['competition_type_id'],
                                     created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar competitions",e)

    @staticmethod
    def delete_competitions():
        compt_list = competition.objects.all()
        for x in compt_list:
            x.delete()

    @staticmethod
    def load_sports():
        """
        Funcion que carga las pruebas almacenados en el archivo json.
        id | name | created_at | updated_at 
        """
        sports_list = json_to_list('sports.json')
        for in_dex in sports_list:
            try:
                sport.objects.create(id=in_dex['id'], name=in_dex['name'],
                                        created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar sports",e)

    @staticmethod
    def delete_sports():
        sports_list = sport.objects.all()
        for x in sports_list:
            x.delete()

class trackInterface():
    @staticmethod
    def load_trackhead2s():
        json_list = json_to_list('trackhead2s.json')
        """
        id | fecha | hora |sport_id | category_id | sex_id | competition_id 
        wind | serie | created_at | updated_at
        """
        for in_dex in json_list:
            try:
                if in_dex['category_id'] == None:
                    in_dex['category_id'] = 1
                
                if in_dex['sex_id'] == None:
                    in_dex['sex_id'] = 1

                if in_dex['sport_id'] == None:
                    in_dex['sport_id'] = 1
                
                track_head2s.objects.create(id=in_dex['id'], fecha=in_dex['fecha'], hora=in_dex['hora'],
                                            sport_id_id=in_dex['sport_id'], category_id_id=in_dex['category_id'], 
                                            sex_id_id=in_dex['sex_id'], competition_id_id=in_dex['competition_id'],
                                            wind=in_dex['wind'], serie=in_dex['serie'],
                                            created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print("Error al cargar track_heads",e)

    @staticmethod
    def delete_trackhead2s():
        trh_list = track_head2s.objects.all()
        for x in trh_list:
            x.delete()

    @staticmethod
    def load_track2s(file):
        json_list = json_to_list(file)
        """
        track_head2s_id | place | achievement | athlete | an | club | region 
        pais | rail | start | bestAchievement | rut | created_at | updated_at
        """
        for in_dex in json_list:
            try:
                if in_dex['an'] == None:
                    in_dex['an'] = 'Nulo'
                if in_dex['pais'] == None:
                    in_dex['pais'] = 'Nulo'
                if in_dex['start'] == None:
                    in_dex['start'] = 'Nulo'
                if in_dex['bestAchievement'] == None:
                    in_dex['bestAchievement'] = 'Nulo'    
                if in_dex['rut'] == None or in_dex['rut'] == "" or in_dex['rut'] == "-":
                    in_dex['rut'] = 'Nulo'  

                track2s.objects.create(id=in_dex['id'], track_head2s_id_id=in_dex['track_head2_id'],
                    place=in_dex['place'], achievement=in_dex['achievement'], athlete=in_dex['athlete'],
                    an=in_dex['an'], club=in_dex['club'], region=in_dex['region'], pais=in_dex['pais'],
                    rail=in_dex['rail'], start=in_dex['start'], bestAchievement=in_dex['bestAchievement'],
                    rut=in_dex['rut'], created_at=in_dex['updated_at'], updated_at=in_dex['updated_at'])
            except Exception as e:
                print(e)

    @staticmethod
    def delete_track2s():
        trk_list = track2s.objects.all()
        for x in trk_list:
            x.delete()
            
    @staticmethod
    def review_results():
        alist = track2s.objects.all()
        #trackInterface.find_rut_errors(alist)
        trackInterface.detect_fails(alist)

    @staticmethod
    def find_rut_errors(alist):
        print("Buscando errores en los ruts",len(alist))
        large_rut = {}
        new = ''
        for i in alist:
            large = str(len(i.rut))
            if large =='11':
                print(i.id,i.rut)
            #new = repair_rut(i.rut)
            #i.rut = new
            #i.save()
            if large_rut.get(large):
                large_rut[str(large)]+=1
            else:
                large_rut[str(large)]=1
        
        text = "Tamaño de los ruts: \n"
        for keys,values in large_rut.items():
            text+= "%s Digitos: %s \n"%(keys,values)
        text += "Tamaño de 9 = 123456789 -> 12.345.678-9 \nTamaño de 12 -> 12.345.678-9 \nTamaño de 8 = 12345678 -> 1.234.567-8"

        print(text)
    
    @staticmethod
    def detect_fails(alist,option='fail'):
        if option == 'fail':
            fail = 0
            for x in alist:
                fail += detect_fail_rut(x.rut)
            print("fallos totales",fail)
        

class newInterface():
    @staticmethod
    def load_new_results(file):
        json_list = json_to_list(file)
        for in_dex in json_list:
            if in_dex['athlete'] == None:
                    in_dex['athlete'] = 'Vacio'
            try: 
                resume_track.objects.create(id=in_dex['id'],trackhead2s_id=in_dex['track_head2_id'],athlete=in_dex['athlete'])
            except Exception as e:
                print(e)

    @staticmethod
    def delete_new_results():
        resume_list = resume_track.objects.all()
        for x in resume_list:
            x.delete()
    
    @staticmethod
    def compare():
        emptyJ,emptyT,emptyTH= 0,0,0
        foundJ,foundT,foundTH = 0,0,0
        empty,found = 0,0
        athletes = athlete.objects.all()

        for x in athletes:
            name = x.names+' '+x.surnames
            queryT = track2s.objects.filter(athlete=name)
            queryHJ = resume_Hjump.objects.filter(athlete=name)
            queryJ = resume_jump.objects.filter(athlete=name)
            queryTH = resume_throw.objects.filter(athlete=name)
            total = 0

            if len(queryT)==0:
                emptyT+=1
            if len(queryHJ)==0 and len(queryJ)==0:
                emptyJ+=1
            if len(queryTH)==0:
                emptyTH+=1

            if len(queryT)==0 and len(queryHJ)==0 and len(queryJ)==0 and  len(queryTH)==0:
                print("no hay registros de el",x.id,x.names,x.surnames)
                empty+=1
            else:
                found+=1
            if empty ==10:
                break
            #print("buscando al atleta",name,"encontados",len(query))
        print("atletas no encotrados",empty)
        print("atletas encontrados",found)
        print("atletas NO encontrados en pista",emptyT)
        print("atletas NO encontrados en salto",emptyJ)
        print("atletas NO encontrados en lanzamiento",emptyTH)

    @staticmethod
    def repair_athletes(option='track'):
        selected = {'track':track2s,'hjump':resume_Hjump,'jump':resume_jump,'throw':resume_throw}
        results = selected[option].objects.all()
        
        for x in results:
            if isinstance(x.athlete,str):
                name = x.athlete.split(' ')
                if x.athlete == '':
                        pass
                elif '' in name:
                    print(x.id,name,"largo",len(x.athlete))
                    new = delete_trashlist(name)
                    new_name = repair_trash(new)
                    print(new,new_name,"largo",len(new_name))
                    x.athlete = new_name
                    x.save()
            
class throwInterface():
    @staticmethod
    def load_throwhead2s():
        pass
    @staticmethod
    def delete_throwhead2s():
        pass
    @staticmethod
    def load_throw():
        pass
    @staticmethod
    def delete_throw():
        pass
    @staticmethod
    def load_resumeThrow(file):
        json_list = json_to_list(file)
        for in_dex in json_list:
            try:
                if in_dex['athlete'] == None:
                   in_dex['athlete'] = 'Vacio'
                
                resume_throw.objects.create(id=in_dex['id'], throwhead=in_dex['throw_head2_id'],
                                            athlete=in_dex['athlete'])
            except Exception as e:
                print(e)
    @staticmethod
    def delete_resumeThrow():
        throws = resume_throw.objects.all()
        for x in throws:
            x.delete()

class jumpInterface():
    @staticmethod
    def load_jumpHead2s():
        pass
    @staticmethod
    def delete_jumoHead2s():
        pass
    @staticmethod
    def load_jump():
        pass
    @staticmethod
    def delete_jump():
        pass
    @staticmethod
    def load_resumeJump(file):
        json_list = json_to_list(file)
        for in_dex in json_list:
            try:
                if in_dex['athlete'] == None:
                   in_dex['athlete'] = 'Vacio'

                if file == 'hjump2s.json':
                    jump = 'hjump_head2_id'
                    resume_Hjump.objects.create(id=in_dex['id'], jumphead=in_dex[jump],
                                            athlete=in_dex['athlete'])
                elif file == 'jump2s.json':
                    jump = 'jump_head2_id'
                    resume_jump.objects.create(id=in_dex['id'], jumphead=in_dex[jump],
                                                athlete=in_dex['athlete'])
            except Exception as e:
                print(e)

    @staticmethod
    def delete_resumeJump():
        jumps = resume_jump.objects.all()
        hjumps = resume_Hjump.objects.all()
        for x in jumps:
            x.delete()
        for y in hjumps:
            y.delete()