from os import stat
from django.db import models

class Countries(models.Model):
    pass

class Regions(models.Model):
    pass

class RgionalAsociations(models.Model):
    pass

class Clubs(models.Model):
    clubName = models.CharField(max_length=200,null=False,blank=False,default='CLUB')

    def __str__(self):
        return "%s %s"%(self.clubName,self.id)


class MembersFactory():
    @staticmethod
    def get_all_clubs():
        club_list = Clubs.objects.all()
        return club_list