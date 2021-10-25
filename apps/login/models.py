from django.db import models
from django.contrib.auth.models import User

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

class absUser(models.Model):
    """clase abstracta de los administradores"""
    logUser = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    class Meta:
        abstract=True

class superAdmin(absUser):
    pass

class fedachiAdmin(absUser):
    pass

class judge(absUser):
    pass

class trackAdmin(absUser):
    pass

class resultsAdmin(absUser):
    pass

class asociationAdmin(absUser):
    pass

class clubAdmin(absUser):
    pass


class userInterface():
    @staticmethod
    def get():
        pass
    @staticmethod
    def set():
        pass

