from functools import total_ordering
from django.db import models

class championships(models.Model):
    championshipName = models.CharField(max_length=200,null=False,blank=False,default='Campeonato ..')

    def __str__(self):
        return "ID: %s | NOMBRE: %s"%(self.id,self.championshipName)

    def name(self):
        return self.championshipName.upper()

class stages(models.Model):
    champId = models.ForeignKey(championships,null=False,blank=False,on_delete=models.CASCADE)
    stageName = models.CharField(max_length=200,null=False,blank=False,default="Etapa ..")

    def __str__(self):
        return "ID:%s | %s | %s"%(self.id,self.stageName,self.champId.championshipName)

    def name(self):
        return self.stageName.upper()

class championshipLogs(models.Model):
    pass

class stageLogs(models.Model):
    pass

class championshipInterface():
    @staticmethod
    def get_champ(c_id):
        champ = championships.objects.get(id=c_id) 
        return champ

    @staticmethod
    def get_total_champ(c_id):
        champQ = championships.objects.get(id=c_id)
        stagesQ = champQ.stages_set.all()
        totalStages = []
        for data in stagesQ:
            competitionsQ = list(data.competitions_set.all().order_by('initDate'))
            if len(competitionsQ) >0:
                compQ = {'stage':data,'competitions':competitionsQ}
            else:
                compQ = {'stage':data,'competitions':''}
            totalStages.append(compQ)
        
        return champQ,totalStages