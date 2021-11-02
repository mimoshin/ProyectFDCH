from django.db import models
from django.db.models.fields import NOT_PROVIDED
from openpyxl import load_workbook
from openpyxl.descriptors import serialisable
from athletes.models import*

DGENERO = {'F':'Damas','M':'Varones'}
DATA = [
        ['10000 marcha','M','08:00','02-10-2021'],
        ['10000 marcha','F','08:00','02-10-2021'],
        ['100 Decatlon',None,'09:00','02-10-2021'],
        ['5000','F','09:15','02-10-2021'],
        ['100V Heptatlon',None,'10:00','02-10-2021'],
        ['100v','F','10:10','02-10-2021'],
        ['110v','M','10:25','02-10-2021'],
        ['5000','M','10:40','02-10-2021'],
        ['100', 'F','11:10','02-10-2021'],
        ['100', 'M','11:50','02-10-2021'],
        ['400', 'F','14:45','02-10-2021'],
        ['400', 'M','15:00','02-10-2021'],
        ['200 Heptatlon',None, '15:30','02-10-2021'],
        ['400 Decatlon',None,'15:45','02-10-2021'],
        ['1500','F','16:00','02-10-2021'],
        ['1500','M','16:30','02-10-2021'],
        ['4x100', 'F' ,'16:40','02-10-2021'],
        ['4x100', 'M','16:50','02-10-2021'],
        ['400v', 'M','17:00','02-10-2021'],
        ['3000','M','08:30','03-10-2021'],
        ['10000','M','08:30','03-10-2021'],
        ['110v Decatlon',None,'09:00','03-10-2021'],
        ['200','F','09:25','03-10-2021'],
        ['200','M','10:00','03-10-2021'],
        ['3000','F','11:20','03-10-2021'],
        ['800','F','11:35','03-10-2021'],
        ['800','M','11:55','03-10-2021'],
        ['800 Heptatlon',None,'12:40','03-10-2021'],
        ['3000 c/o','F','12:50','03-10-2021'],
        ['3000 c/o','M','13:10','03-10-2021'],
        ['4x400','F' ,'13:30','03-10-2021'],
        ['4x400','M','13:40','03-10-2021'],
        ['1500 Decatlon',None,'13:50','03-10-2021'],
        ['400v','F','17:00','03-10-2021'],
        ]


# Create your models here.
class linea_excel(models.Model):
    atleta = models.CharField(max_length=200)
    materno = models.CharField(max_length=200)
    paterno = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    prueba = models.CharField(max_length=200)
    serie = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200)
    pista = models.CharField(max_length=200)
    rail = models.CharField(max_length=200)

    def __str__(self):
        return "ATLETA QUE CORRE %s - %s - SERIE %s"%(self.prueba,self.sexo,self.serie)
    def get_evet(self):
        if self.pista == '.':
            pist = self.rail 
        else: 
            pist = self.pista
        if self.serie == str(1) and self.prueba == (100):
            print("nose que pasa aqui")
            #1,2,3,4,5,6,7,8,9,10,11,12
        apellidos = self.paterno+' '+self.materno
        texto = ',0,%s,%s,%s,%s,,%s,,,,,%s \n'%(pist,apellidos,self.atleta,self.club,self.region,self.rut)
        return texto


class horario(models.Model):
    eventName = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)

    def __str__(self):
        return "prueba: %s - %s - %s"%(self.eventName,self.genero,self.hora)
    def get_genero(self):
        if self.genero == 'F' or self.genero == 'M':
            return DGENERO[self.genero]
        else:
            return ' '

class interfaz():
    @staticmethod
    def cargar_excel():
        archivo = load_workbook('C:\\LecturaU20.xlsx')
        planillas = archivo['RES TODOS']
        for num in range(2,497):
            Iprueba = 'K'+str(num)
            Igenero = 'E'+str(num)
            Iatleta = 'D'+str(num)
            Iserie = 'L'+str(num)
            Irut = 'F'+str(num)
            Ipista = 'N'+str(num)
            Irail = 'AL'+str(num)
            Imaterno = 'C'+str(num)
            Ipaterno = 'B'+str(num)
            Iclub = 'I'+str(num)
            Iregion = 'J'+str(num)

            lprueba = str(planillas[Iprueba].value)
            lgenero = planillas[Igenero].value
            latleta = planillas[Iatleta].value
            lserie = planillas[Iserie].value
            lrut = planillas[Irut].value
            lpista = planillas[Ipista].value
            lrail = planillas[Irail].value
            lmaterno = planillas[Imaterno].value
            lpaterno = planillas[Ipaterno].value
            lclub = planillas[Iclub].value
            lregion = planillas[Iregion].value
            if lserie == None:
                lserie = '1'
            if  lpista == None:
                lpista = '.'
            if  lrail == None:
                lrail = '.'
            if lclub == None:
                lclub = '.'
            if lregion == None:
                lregion = '.'
            if lmaterno == None:
                lmaterno  = ' '
            if lpaterno == None:
                lpaterno = ' '
            elif '+=' in str(lrail) or '=+' in str(lrail):
                lrail = '.'

            linea_excel.objects.create(atleta=latleta,materno=lmaterno,paterno=lpaterno,club=lclub,prueba=lprueba,serie=lserie,rut=lrut,
                                        sexo=lgenero,pista=lpista,rail=lrail,region=lregion)
    @staticmethod
    def cargar_todo():
        lista = linea_excel.objects.all()
        return lista
    @staticmethod
    def filtrar(filtro,genero):
        texto = open('C:/Users/Franco/Desktop/ejemplos/Lynx.evt','w+',encoding='utf-8')
        sabado,domingo = interfaz.generarEVT()
        todos = linea_excel.objects.all()
        total_sabado = len(sabado)
        total_domingo = len(domingo)

        for x in range(0,total_sabado):
            linea = sabado[x]

            series =  interfaz.contar_series(linea.eventName,linea.genero)
            pruebas = todos.filter(prueba=linea.eventName,sexo=linea.genero)
            dgenero = linea.get_genero()
            if linea.eventName == '1500':
                print("quiere cargar los 1500")
            if series == 1 :
                stringado = '1,'+str(x+1)+','+str(1)+','+linea.eventName+' '+dgenero+' - Serie 1 - '+linea.hora+' HORAS\n' 
                texto.writelines(stringado)
                #print("total de lineas %s"%(len(pruebas)))
                for y in pruebas:
                    texto.writelines(y.get_evet())

            elif series > 1 :
                for a in range(series):
                    stringado = '1,'+str(x+1)+','+str(a+1)+','+linea.eventName+' '+dgenero+' - Serie '+str(a+1) +' - '+linea.hora+' HORAS\n' 
                    texto.writelines(stringado)
                    for z in pruebas:
                        if z.serie == str(a+1):
                            texto.writelines(z.get_evet())

        for x in range(0,total_domingo):
            linea = domingo[x]

            series =  interfaz.contar_series(linea.eventName,linea.genero)
            pruebas = todos.filter(prueba=linea.eventName,sexo=linea.genero)
            dgenero = linea.get_genero()

            if series == 1 :
                stringado = '2,'+str(x+1)+','+str(1)+','+linea.eventName+' '+dgenero+' - Serie 1 - '+linea.hora+' HORAS\n' 
                texto.writelines(stringado)
                #print("total de lineas %s"%(len(pruebas)))
                for y in pruebas:
                    texto.writelines(y.get_evet())

            elif series > 1 :
                for a in range(series):
                    stringado = '2,'+str(x+1)+','+str(a+1)+','+linea.eventName+' '+dgenero+' Serie '+str(a+1)+' - '+linea.hora+' HORAS\n'
                    texto.writelines(stringado)
                    for z in pruebas:
                        if z.serie == str(a+1):
                            texto.writelines(z.get_evet())
        texto.close()

        filtrados = todos.filter(prueba=filtro,sexo=genero).order_by('serie')
        return filtrados

    @staticmethod
    def cargar_hora():
        for x in DATA:
            if x[1] == None:
                x[1] =' '
            horario.objects.create(eventName=x[0],genero=x[1],hora=x[2],fecha=x[3])

    @staticmethod
    def generarEVT():
        sabado = horario.objects.filter(fecha='02-10-2021')
        domingo = horario.objects.filter(fecha='03-10-2021')
        return sabado,domingo
        
    @staticmethod
    def contar_series(prueb,sexo):
        series=[]
        lista = linea_excel.objects.filter(prueba=prueb)
        for x in lista:
            if x.serie == '.':
                break
            if x.serie not in series:
                series.append(x.serie)

        if len(series) == 0:
            #print("la prueba %s %s tiene %s series"%(prueb,sexo,1))
            return 1
        elif len(series)>0:
            #print("la prueba %s %s tiene %s series"%(prueb,sexo,len(series)))
            return len(series)

    @staticmethod
    def cargar_hepta():
        pass