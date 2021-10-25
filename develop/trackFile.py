from django.db import models
from .competitionFile import categories,competition,sport
from .sharedModels import categories,sexes

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
    track_head2s_id = models.ForeignKey(track_head2s,  on_delete=models.CASCADE, null=False, blank=False)
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
        return "TH2: %s | lugar %s | marca %s"%(self.track_head2s_id,self.place,self.achievement)