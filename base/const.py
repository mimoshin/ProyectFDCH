#.............CONSTANTS CHOICES............................

GENDER_CHOICES = ((0,'SIN GENERO'),(1,'DAMAS'),(2,'VARONES'))

EVENT_TYPE_CHOICES = ((1,'VELOCIDAD'),(2,'MEDIOFONDO'),(3,'SALTO'),(4,'GARROCHA'),(5,'LANZAMIENTO'))

FILE_TYPE = {1:'Planilla Velocidad.xlsx',2:'Planilla Mediofondo.xlsx',3:'Planilla Salto.xlsx',
                 4:'Planilla Garrocha.xlsx',5:'Planilla Lanzamientos.xlsx'}

ROUND_CHOICES = ((0,'DF'),(1,'SERIE'),(2,'SEMIFINAL'),(3,'FINAL'))

FEDACHI_LOGO = "C:/Users/Franco/Desktop/Proyectos/Fedachi/Codigo/panamU20/primera_version/static/img/logo.png"

RANDON_RANGES = {1:(10.5,11.9), 2:(19.80,23.2), 3:(44.5,65.5), 4:(11.2,13.5), 5:(11.2,13.5), 6:(44.5,65.5),
    7:(105.0,120.9), 8:(210.0,240.9), 9:(720.0,1080.9), 10:(1680.0,2040.9), 11:(4.5,8.5), 12:(12.0,18,9),
    13:(1.7,2.2), 14:(4.0,6.15), 15:(65.0,85.9), 16:(15.0,21.9), 17:(55.0,68.9), 18:(60.0,80.9)}
"""
RANDON_RANGES = [
	{"id" : 1,"name" : "100 METROS PLANOS","range" : (10.5,11.9)},
	{"id" : 2,"name" : "200 METROS PLANOS","range" : (19.80,23.2)},
	{"id" : 3,"name" : "400 METROS PLANOS","range" : (44.5,65.5)},
	{"id" : 4,"name" : "100 METROS CON VALLAS","range" : (11.2,13.5)},
	{"id" : 5,"name" : "110 METROS CON VALLAS","range" : (11.2,13.5)},
	{"id" : 6,"name" : "400 METROS CON VALLAS","range" : (44.5,65.5)},
	{"id" : 7,"name" : "800 METROS PLANOS","range" : (105.0,120.9)},
	{"id" : 8,"name" : "1500 METROS PLANOS","range" : (210.0,240.9)},
	{"id" : 9,"name" : "5000 METROS PLANOS","range" : (720.0,1080.9)},
	{"id" : 10,"name" : "10000 METROS PLANOS","range" : (1680.0,2040.9)},
	{"id" : 11,"name" : "SALTO LARGO","range" : (4.5,8.5)},
	{"id" : 12,"name" : "SALTO TRIPLE","range" : (12.0,18,9)},
	{"id" : 13,"name" : "SALTO ALTO","range" : (1.7,2.2)},
	{"id" : 14,"name" : "SALTO CON GARROCHA","range" : (4.0,6.15)},
	{"id" : 15,"name" : "LANZAMIENTO DE LA JABALINA","range" : (65.0,85.9)},
	{"id" : 16,"name" : "LANZAMIENTO DE LA BALA","range" : (15.0,21.9)},
	{"id" : 17,"name" : "LANZAMIENTO DEL DISCO","range" : (55,0,68.9)},
	{"id" : 18,"name" : "LANZAMIENTO DEL MARTILLO","range" : (60.0,80.9)}
]
"""

#..........................................................