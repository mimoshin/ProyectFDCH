from apps.login.views import user_logout
from django.db import models
from django.contrib.auth.models import User


class IUser(models.Model):
    """
    Clase abstracta escrita para el "compartimiento de variales" | evaluar su uso
    """
    log_user = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    #one_user = models.OneToOneField(User,nu)
    class Meta:
        abstract=True
        

class Super_admin(IUser):
    pass

class Fed_admin(IUser):
    pass

class Asociation_admin(IUser):
    pass

class Club_admin(IUser):
    pass

class Users_Interface():
    @staticmethod
    def get():
        pass
    @staticmethod
    def set():
        pass


