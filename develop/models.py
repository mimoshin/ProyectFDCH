from django.db import models


class results(models.Model):
    id_or = models.CharField(max_length=200,null=True,blank=True)
    campeonato = models.CharField(max_length=200,null=True,blank=True)
    prueba = models.CharField(max_length=200,null=True,blank=True)
    serie = models.CharField(max_length=200,null=True,blank=True)
    pista = models.CharField(max_length=200,null=True,blank=True)
    atleta = models.CharField(max_length=200,null=True,blank=True)
    marca = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return "%s - %s - %s"%(self.atleta,self.prueba,self.marca)

class best_mark(models.Model):
    atleta = models.CharField(max_length=200,null=True,blank=True)
    prueba = models.CharField(max_length=200,null=True,blank=True)
    marca = models.CharField(max_length=200,null=True,blank=True)



class Track_Interface():

    @staticmethod
    def load_results(c_id):
        try:
            rlist = track2s.objects.filter(track_head2s_id__competition_id__stage_id__championship_id__id=c_id).order_by('athlete')
        except Exception as e:
            rlist = []
            print("Fallo la carga de resultados",e)
        return rlist
    
    @staticmethod
    def charge_results(c_id):
        rlist = Track_Interface.load_results(c_id)
        print(len(rlist))
        for ind in rlist:
            try:
                id_or = ind.id
                campeonato = ind.track_head2s_id.competition_id.stage_id.championship_id.id
                prueba = ind.track_head2s_id.competition_id.sport_id.name
                serie = ind.track_head2s_id.serie +' '+str(ind.track_head2s_id.competition_id.id)
                pista = ind.rail
                atleta = ind.athlete
                marca = ind.achievement
                results.objects.create(id_or=id_or, campeonato=campeonato, prueba=prueba, serie=serie,
                                pista=pista, atleta=atleta, marca=marca)
            except Exception as e:
                print('error al cargar results',e)

    @staticmethod
    def delete_results(c_id):
        rlist = results.objects.all()
        for x in rlist:
            x.delete()

    @staticmethod
    def load_all_results():
        try:
            rlist = track2s.objects.all()
        except Exception as e :
            rlist =[]
            print("Fallo la carga de resultados",e)
        return rlist

    @staticmethod
    def delete_all_results():
        rlist = results.objects.all()
        for x in rlist:
            x.delete()
