from django.db import models
from django.db.models.base import Model

# Create your models here.
"""
Perfiles FEDACHI
admin -> SuperAdmin(Acceso a todo)
sub_admin -> Administrador(Acceso a ver todo, CRUD limitado)
admin_results -> Digitador(Acceso solo a tipeo de resultados)
admin_track -> Camara de llamados(Acceso a todo lo relacionado a pista)
judge -> Jueces(Acceso a lo correspondiente)
"""

class admin(models.Model):
    pass

class sub_admin(models.Model):
    pass

class admin_results(models.Model):
    pass

class admin_track(models.Model):
    pass

class admin_region(models.Model):
    pass

class admin_club(models.Model):
    pass


class Admins_Interface():
    @staticmethod
    def get_function():
        pass
    @staticmethod
    def set_function():
        pass

