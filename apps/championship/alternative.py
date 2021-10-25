from django.db import models
from django.db.models.base import Model
from django.utils import timezone

class championship(models.Model):
    # ID	NOMBRE_CAMPEONATO	FECHA_INICIO	FECHA_TERMINO	REGION	PAIS	DIRECCION
    event_name = models.CharField(max_length=50, null=False, default='NOMBRE_CAMPEONATO') 
    init_date = models.DateTimeField(default=timezone.now(), null=False)
    finish_date = models.DateTimeField(default=timezone.now(), null=False)
    region = models.CharField(max_length=50, null=False, default='REGION')
    country = models.CharField(max_length=50, null=False, default='PAIS')
    direction = models.CharField(max_length=50, null=False, default='DIRECCION')

    def __str__(self):
        return "%s" % (self.event_name)

class champ_log(models.Model):
    # ID	CAMPEONATO	FECHA	LOG	ADMIN
    champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate(), null=False)
    log = models.CharField(max_length=200, default='CAMBIO REALIZADO')
    admin = models.CharField(max_length=20, default='ADMIN', null=False) #LLAVE FORANEA ADMIN

class category(models.Model):
    # ID	NOMBRE_CATEGORIA	SIGLA_CATEGORIA
    category_name = models.CharField(max_length=10, null=False, default='CATEGORIA I')
    category_flag = models.CharField(max_length=10, null=False, default='GGWP')

class champ_category(models.Model):
    # Campeonato	Categoria
    champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE)
    categ_fk = models.ForeignKey(category, null=False, blank=False, on_delete=models.CASCADE)


class stage(models.Model):
    # ID	NOMBRE_ETAPA	CAMPEONATO	FECHA	HORA_INICIO     HORA_FIN    CREADOR	    NUM_COMPT	ETAPA_NUM
    stage_name = models.CharField(max_length=30, default='NOMBRE_ETAPA')
    champ_fk = models.ForeignKey(championship, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate())
    init_hour = models.TimeField(default='08:00:00')
    finish_hour = models.TimeField(default='00:00:00')
    creator = models.CharField(max_length=30, default='ADMIN')
    num_compt = models.IntegerField(default=1)
    stage_num = models.IntegerField(default=1)

class stage_log(models.Model):
    # ID	ETAPA	FECHA	LOG	ADMIN
    stage = models.ForeignKey(stage, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate(), null=False)
    log = models.CharField(max_length=20, default='CAMBIO REALIZADO')
    admin = models.CharField(max_length=20, default='ADMIN', null=False) #LLAVE FORANEA ADMIN

class test(models.Model):
   # ID	NOMBRE_PRUEBA TIPO
   test_name = models.CharField(max_length=20, null=False, default='PRUEBA X')
   type_test = models.CharField(max_length=20, null=False, default='TIPO X')


class competition(models.Model):
    # ID	ETAPA	PRUEBA	HORA	CATEGORIAS	GENERO
    stage_fk = models.ForeignKey(stage, null=False, blank=False, on_delete=models.CASCADE)
    tets_fk = models.ForeignKey(test, null=False, blank=False, on_delete=models.CASCADE)
    hour = models.TimeField(default='08:00', null=False, blank=False)
    categorys = models.IntegerField(default=11111)
    gender = models.CharField(max_length=10, default='GENERO')

class inscription(models.Model):
    # ID	ATLETA	COMPETICION	MARCA
    athlete = models.CharField(max_length=10, default='ATLETA')
    compt_fk = models.ForeignKey(competition, null=False, blank=False, on_delete=models.CASCADE)
    mark = models.DecimalField(default=00.01)

class track_series(models.Model):
    # ID	INSCRIPCION	PISTA	NUM_SERIE	RESULTADO
    inscription = models.ForeignKey(inscription, null=False, blank=False, on_delete=models.CASCADE)
    pist = models.IntegerField(default=0)
    serie_num = models.IntegerField(default=0)
    result = models.DecimalField(default=00.01)

class serie(models.Model):
    # ID	COMPETENCIA	NUM_SERIE VIENTO
    competition_fk = models.ForeignKey(competition,null=False, blank=False, on_delete=models.CASCADE)
    num_serie = models.IntegerField(default=1)
    wind = models.CharField(max_length=6, default='00.00')

class asignation(models.Model):
    # ID	SERIE	ATLETA	PISTA	MARCA	RESULTADO
    serie_fk = models.ForeignKey(serie, null=False, blank=False, on_delete=models.CASCADE)
    athlete_fk = models.CharField(max_length=30)
    pist = models.IntegerField(default=1)
    mark = models.CharField(max_length=20, default='99.99py')
    result = models.CharField(max_length=20, default='00.00')





