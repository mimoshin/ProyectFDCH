from django.db import models
from django.contrib.auth.models import User

class absUser(models.Model):
    """clase abstracta de los administradores"""
    logUser = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    class Meta:
        abstract=True
        
class superAdmin(absUser):
    pass

class fedachiAdmin(absUser):
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





