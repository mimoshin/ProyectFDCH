from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

"""
Perfiles FEDACHI
    superAdmin      -> SuperAdmin (Acceso a todo)
    fedachiAdmin    -> Administrador (Acceso a ver todo, CRUD limitado)
    resultsAdmin    -> Digitador (Acceso solo a tipeo de resultados)
    trackAdmin      -> Camara de llamados (Acceso a todo lo relacionado a pista)
    judge           -> Jueces (Acceso a lo correspondiente)
    asociationAdmin -> Asociaciones regionales (Acceso a lo correspondiente)
    clubAdmin       -> Clubes (Acceso a lo correspondiente)
"""

# Create your models here.
class absUser(models.Model):
    """clase abstracta de los administradores"""
    logUser = models.ForeignKey(User,null=False,related_name="%(class)s",blank=False,on_delete=models.CASCADE)
    class Meta:
        abstract=True
    def __str__(self):
        return "__AbstractName__"
        
class SuperAdmin(absUser):
    pass

class FedachiAdmin(absUser):
    pass

class AsociationAdmin(User):
    pass

class ClubAdmin(absUser):
    pass

class Judge(absUser):
    pass

class TrackAdmin(absUser):
    pass

class ResultsAdmin(absUser):
    pass


class UserFactory():
    @staticmethod
    def get():
        pass
    @staticmethod
    def get_type_user(name):
        user = User.objects.get(username=name)
        if user.fedachiadmin.all():
            return [True,"Fedachi"]
        elif user.resultsadmin.all():
            print("resultados")
        else:
            return [False,"Anonimo"]

    @staticmethod
    def get_type_user2(name):
        user = User.objects.get(username=name)
        if user.fedachiadmin.all():
            return "Fedachi"
        elif user.resultsadmin.all():
            print("resultados")
        else:
            return False
            
    @staticmethod
    def set():
        pass
