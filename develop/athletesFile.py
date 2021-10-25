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
    
    def separate_names(self):
        total = self.names.split(' ')
        text = ''
        for x in total:
            if not x:
                text += '<td>ESPACIO</td>'    
            text += '<td>'+x+'</td>'
        return text

    def get_de(self):
        data = self.names 
        if ' DE ' in data or ' de ' in data or ' DEL ' in data or ' del 'in data:
            #print(self.names.split(' '))
            return True
        else:
            return False

    def get_de_los(self):
        data = self.names 
        if ' DE LOS ' in data or ' DE LAS ' in data:
            #print(self.names.split(' '))
            return True
        else:
            return False

    def total_names(self):
        total = self.names.split(' ')
        names =[]

        if self.get_de_los():
            #print(total, len(total)-2)
            if len(total)-2 == 2:
                first_name = total[0]
                second_name =''
                for x in total[1:]:
                    second_name+= x +' '
                if ord(second_name[-1]) ==32:
                    second_name = second_name[:-1]
                
                names.append(first_name)
                names.append(second_name)
                #print("first",first_name)
                #print("second",second_name)
        
        elif self.get_de():
            #print(total, len(total)-1)
            if len(total)-1 > 2:
                first_name = total[0]
                second_name = total[1]
                third_name = ''
                for x in total[2:]:
                    third_name+= x +' '
                if ord(third_name[-1]) ==32:
                    third_name = third_name[:-1]
                
                names.append(first_name)
                names.append(second_name)
                names.append(third_name)
                #print("first",first_name)
                #print("second",second_name)
                #print("third", third_name)
            
            elif len(total)-1 == 2:
                first_name = total[0]
                second_name =''
                for x in total[1:]:
                    second_name+= x +' '
                if ord(second_name[-1]) ==32:
                    second_name = second_name[:-1]
                
                names.append(first_name)
                names.append(second_name)
                #print("first",first_name)
                #print("second",second_name)
        else:
            #print(total, len(total))
            if len(total) == 1:
                first_name = total[0]
                names.append(first_name)
                #print("first",first_name)
            elif len(total) == 2:
                first_name = total[0]
                second_name = total[1]

                names.append(first_name)
                names.append(second_name)
                #print("first",first_name)
                #print("second",second_name)
            elif len(total) == 3:
                #print(total, len(total))
                first_name = total[0]
                second_name = total[1]
                third_name = total[2]
                names.append(first_name)
                names.append(second_name)
                names.append(third_name)
                #print("first",first_name)
                #print("second",second_name)
                #print("third",third_name)
            else:
                pass
                #print(self.id,total, len(total))
        return names
    
    def total_lastnames(self):
        total = self.surnames.split(' ')
        return total

    def repair_name(self):
        total = self.names.split(' ')
        trash = delete_trashlist(total)
        text = repair_trash(trash)
        return text

    def repair_lastname(self):
        total = self.surnames.split(' ')
        trash = delete_trashlist(total)
        text = repair_trash(trash)
        return text
        
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
   

class Athlete_Interface():
    @staticmethod
    def load_athletes(ALITS):
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
    def get_wrong(alist):
        wrongs = 0
        de = 0
        de_los = 0
        for index in alist:
            if index.wrong():
                wrongs+=1
            if index.get_de_los():
                de_los+=1
            elif index.get_de():
                de+=1
        print("Mal escritos -> %s"%(wrongs))
        print("algo DE otro -> %s"%(de))
        print("algo DE LOS x -> %s"%(de_los))
    
    
    @staticmethod
    def detect_wrongs(alist):
        nn_wrongs, nt_wrongs = 0,0
        ln_wrongs, lt_wrongs = 0,0
        for i in alist:
            if null_wrong(i.names):
                nn_wrongs+=1
            if tab_wrong(i.names):
                nt_wrongs+=1
            if null_wrong(i.surnames):
                ln_wrongs+=1
            if tab_wrong(i.surnames):
                lt_wrongs+=1
        print("Nombres mal escritos ->",nn_wrongs)
        print("Nombres mal espaciados -> ",nt_wrongs)
        print("Apellidos mal escritos ->",ln_wrongs)
        print("Apellidos mal espaciados ->", lt_wrongs)
    
    @staticmethod
    def repair_nametext(alist):
        for index in alist:
            if null_wrong(index.names):
                new = index.repair_name()
                index.names = new
                index.save()
            if tab_wrong(index.names):
                new = index.repair_name()
                index.names = new
                index.save()

    @staticmethod
    def repair_lastnametext(alist):
        for index in alist:
            if null_wrong(index.surnames):
                new = index.repair_lastname()
                index.surnames = new
                index.save()
            if tab_wrong(index.surnames):
                new = index.repair_lastname()
                index.surnames = new
                index.save()
    
    @staticmethod
    def find_errors(alist):
        contad = 0
        for x in alist:
            for i in x.surnames:
                error = False
                if ord(i) == 9:
                    error = True  
                if ord(i) == 0:
                    error == True
            if error:
                contad+=1
            print(x.surnames.split(' '))
            for a in x.surnames.split(' '):
                if '' in a:
                    contad+=1
                
        print("errores",contad)
    @staticmethod
    def all_athletes():
        A_LIST = athlete.objects.all()
        #Athlete_Interface.get_wrong(A_LIST)
        #Athlete_Interface.detect_wrongs(A_LIST)
        #Athlete_Interface.repair_nametext(A_LIST)
        #Athlete_Interface.repair_lastnametext(A_LIST)
        #Athlete_Interface.find_errors(A_LIST)
        return A_LIST
    
    @staticmethod
    def delete_all_athletes():
        data = athlete.objects.all()
        for i in data:
            i.delete()
        
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