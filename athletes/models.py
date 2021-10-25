from develop.read_json import write_json
from django.db import models
from .utils import *

# Create your models here.
class athlete(models.Model):
    names = models.CharField(max_length=200,null=True,blank=True)
    surnames = models.CharField(max_length=200,null=True,blank=True)
    sex = models.CharField(max_length=200,null=True,blank=True)
    birthdate = models.CharField(max_length=200,null=True,blank=True)
    birthyear = models.IntegerField(null=True,blank=True)
    rut = models.CharField(max_length=200,null=True,blank=True)
    idclub = models.IntegerField(null=True,blank=True)
    idregion = models.IntegerField(null=True,blank=True)
    cellphone = models.CharField(max_length=200,null=True,blank=True)
    mail = models.CharField(max_length=200,null=True,blank=True)
    idcoach = models.IntegerField(null=True,blank=True)
    size = models.CharField(max_length=200,null=True,blank=True)
    heihgt = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.CharField(max_length=200,null=True,blank=True)
    updated_at = models.CharField(max_length=200,null=True,blank=True)
    sex_id = models.IntegerField(null=True,blank=True)
    region_id = models.IntegerField(null=True,blank=True)
    club_id = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.names

    def repair(self,option='names'):
        selected = {'names':self.names,'surnames':self.surnames} 
        data = selected[option]
        total = data.split(' ')
        trash = delete_trashlist(total)
        text = repair_trash(trash)
        if option =='names':
            self.names = text
            self.save()
        elif option =='surnames':
            self.surnames = text
            self.save()
        return text
    
    def repair_rut(self):
        new_rut = repair_rut(self.rut)
        self.rut = new_rut
        self.save()
        #print(self.rut,new_rut)

class athleteNames(models.Model):
    athleteId = models.ForeignKey(athlete,null=False,blank=False,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200,null=True,blank=True)
    secondName = models.CharField(max_length=200,null=True,blank=True)
    thirdName = models.CharField(max_length=200,null=True,blank=True)
    fourName = models.CharField(max_length=200,null=True,blank=True)
    surname = models.CharField(max_length=200,null=True,blank=True)
    secondSurname = models.CharField(max_length=200,null=True,blank=True)
    thirdSurname = models.CharField(max_length=200,null=True,blank=True)
    fourSurname = models.CharField(max_length=200,null=True,blank=True)
   
class athleteInterface():
    #------- GEt & SET ---------
    @staticmethod
    def all_athletes():
        A_LIST = athlete.objects.all()
        return A_LIST

    #---------------------------

    #------TOOLS & OTHERS ------
    @staticmethod
    def load_athletes(ALITS):
        """
            IMPORTA LOS ATLETAS DESDE EL ARCHIVO .JSON
            ALMACENAS LOS DATOS LEIDOS EN LA BASE DE DATOS
        """
        try:
            for i in ALITS:
                for x in i:
                    if i[x]:
                        pass
                    else:
                        i[x] = None
                athlete.objects.create(id=i['id'], names=i['names'],surnames=i['surnames'],sex=i['sex'],birthdate=i['birthdate'],
                birthyear=i['birthyear'],rut=i['rut'],idclub=i['idClub'],idregion=i['idRegion'],cellphone=i['cellPhone'],mail=i['mail'],
                idcoach=i['idCoach'],size=i['size'],heihgt=i['height'],created_at=i['created_at'],updated_at=i['updated_at'],
                sex_id=i['sex_id'],region_id=i['region_id'],club_id=i['club_id'])
                
        except Exception as e:
            print("error al cargar atletas",e)

    @staticmethod
    def delete_all_athletes():
        data = athlete.objects.all()
        for i in data:
            i.delete()

    @staticmethod
    def review_names():
        #REVISAR NOMBRES COMO X DE LOS Y, A DE B, ETC
        A_LIST = athlete.objects.all()
        find = athleteInterface.find_name_errors(A_LIST)
        detect = athleteInterface.detect_wrong_names(A_LIST)
        data_json = {'find':[find,detect[0]],'result':detect[1]}
        #data_json = {'hola':'hola'}
        return data_json

    @staticmethod
    def find_name_errors(alist):
        """
            Busca caracteres: 
                HORIZONTAL-TAB (ASCII 09) | NULL (ASCII 00)
        """
        contad = 0
        for x in alist:
            aux1,aux2 =0,0
            for i in x.names:
                error = False
                if ord(i) == 9:
                    print('tabulador encontrado')
                    aux1+=1
                    error = True 
            for a in x.names.split(' '): 
                if a == '':
                    aux2+=1
                    error == True
                    print('nulo encontrado')
            if aux1 > 0 or aux2 > 0:
                contad+=1
                #print(x.names.split(' '))
        return 'Errores en general: %s <br>'%(contad)

    @staticmethod
    def detect_wrong_names(alist):
        counters = {'nnw':0,'ntw':0,'lnw':0,'ltw':0}
        for i in alist:
            if null_wrong(i.names):
                counters['nnw']+=1
            if tab_wrong(i.names):
                counters['ntw']+=1
            if null_wrong(i.surnames):
                counters['lnw']+=1
            if tab_wrong(i.surnames):
                counters['ltw']+=1
            if null_wrong(i.names) or tab_wrong(i.names) or null_wrong(i.surnames) or tab_wrong(i.surnames):
                print(i.names.split(' '),i.surnames.split(' '))

        text = "Nombres mal escritos: %s <br> Nombres mal espaciados: %s <br> Apellidos mal escritos: %s <br> Apellidos mal espaciados %s " % \
                (counters['nnw'],counters['ntw'],counters['lnw'],counters['ltw'])

        if counters['lnw']>0 or counters['ltw']>0 or counters['nnw']>0 or counters['ntw'] >0:
            result = text,True
        else:
            result = text,False
        return result

    @staticmethod
    def repair_names(alist,option='names'):
        print("Opcion a reparar",option)
        contador = 0
        for index in alist:
            selected = {'names':index.names,'surnames':index.surnames}
            aux1,aux2=0,0
            if null_wrong(selected[option]):
                new = index.repair(option)
                aux1+=1
            if tab_wrong(selected[option]):
                new = index.repair(option)
                aux2+=1
            if aux1 >0 or aux2 >0:
                contador+=1
                print(selected[option].split(' '),new.split(' '))
        print(contador,option,'con errores.')

    @staticmethod
    def review_rut():
        A_LIST = athlete.objects.all()
        athleteInterface.detect_wrong_ruts(A_LIST)
        result_error = athleteInterface.find_rut_errors(A_LIST) 
        data_json = {'find':result_error,'result':True}
        return data_json

    @staticmethod
    def find_rut_errors(alist):
        print("Buscando errores en los ruts",len(alist))
        large_rut = {}
        new = ''
        for i in alist:
            large = str(len(i.rut))
            if large == '12':
                new = i.rut
            if large_rut.get(large):
                large_rut[str(large)]+=1
            else:
                large_rut[str(large)]=1
        
        text = "Tamaño de los ruts: <br>"
        for keys,values in large_rut.items():
            text+= "%s Digitos: %s <br>"%(keys,values)
        text += "Tamaño de 9 = 123456789 -> 12.345.678-9 <br> Tamaño de 12 -> 12.345.678-9 <br> Tamaño de 8 = 12345678 -> 1.234.567-8"

        return text

    @staticmethod
    def detect_wrong_ruts(alist):
        large_rut = {}
        dg_rut = {}
        for i in alist:
            large = str(len(i.rut))

            if large_rut.get(large):
                large_rut[str(large)]+=1
                dg_rut[str(large)]+=detect_dg(i.rut)
            else:
                large_rut[str(large)]=1
                dg_rut[str(large)]=detect_dg(i.rut)
                
        print(large_rut)
        print(dg_rut)

    @staticmethod
    def repair_ruts(alist):
        for x in alist:
            x.repair_rut()

    @staticmethod
    def gen_json():
        data = {'athletes':[]}
        alist = athlete.objects.all().order_by('names')
        for x in alist:
            dictio ={   'id':x.id,
                        'name':x.names,
                        'surnames':x.surnames,
                        'rut':x.rut
                    }
            data['athletes'].append(dictio)
        
        write_json(data,'data.json')
     #---------------------------







    @staticmethod
    def new_athletes(alist):
        # 213 | 1202 | 2534 especiales | 1137 | 1309
        # de la | san martin | de 
        data = []
        one,two,three, other = 0,0,0,0
        for x in alist:
            new_dict = {'id':x.id}
            names = x.total_names()
            if len(names) == 1:
                new_dict['firstname'] = names[0]
                new_dict['secondname'] = None
                new_dict['thirdnames'] = None
                new_dict['fourname'] = None
            elif len(names) == 2:
                new_dict['firstname'] = names[0]
                new_dict['secondname'] = names[1]
                new_dict['thirdnames'] = None
                new_dict['fourname'] = None
            elif len(names) == 3:
                new_dict['firstname'] = names[0]
                new_dict['secondname'] = names[1]
                new_dict['thirdnames'] = names[2]
                new_dict['fourname'] = None
            
            lastnames = x.total_lastnames()
            if len(lastnames) == 1:
                new_dict['fi_lastnames'] = lastnames[0]
                new_dict['se_lastnames'] = None
                new_dict['th_lastnames'] = None
                new_dict['fo_lastnames'] = None
            elif len(lastnames) == 2:
                new_dict['fi_lastnames'] = lastnames[0]
                new_dict['se_lastnames'] = lastnames[1]
                new_dict['th_lastnames'] = None
                new_dict['fo_lastnames'] = None
            else:
                new_dict['fi_lastnames'] = x.surnames
                new_dict['se_lastnames'] = None
                new_dict['th_lastnames'] = None
                new_dict['fo_lastnames'] = None

            new_dict['rut'] = x.rut
            new_dict['birthdate'] = x.birthdate
            new_dict['cellPhone'] = x.cellphone
            new_dict['mail'] = x.mail
            new_dict['size'] = x.size
            new_dict['height'] = x.heihgt
            new_dict['created_at'] = x.created_at
            new_dict['updated_at'] = '19-08-2021 20:00:00'
            new_dict['sex_id'] = x.sex_id
            new_dict['region_id'] = x.region_id
            new_dict['club_id'] = x.club_id 

            data.append(new_dict)
        return data

