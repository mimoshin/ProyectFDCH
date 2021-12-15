import datetime
from django import forms

""" 
    ********************************
    **--LIMITE DE ATLETAS         **
    **  POR CLUB EN UNA PRUEBA----**
    ********************************
    **  0 = Sin Limite            **
    **  1 = 1 Atleta por prueba   **
    **  2 = 2 Atletas por prueba  **
    **  3 = 3 Atletas por prueba  **
    **  4 = 4 Atletas por prueba  **
    **  5 = 5 Atletas por prueba  **
    ********************************

    *****************************************
    **----LIMITE DE PRUEBAS POR ATLETA-----** 
    *****************************************
    **  0 = Sin Limite                     **
    **  2 = 2 Pruebas Individuales         **
    **  21 = 2 Pruebas Individuales + Posta**
    **  3 = 3 Pruebas Individuales         **
    **  31 = 3 Pruebas Individuales+ Posta **
    *****************************************

    *****************************************
    **--------------CATEGORIAS-------------** 
    *****************************************
    **  M = Master                         **
    **  A = Adulto                         **
    **  CD = Capacidades Diferentes        **
    **  TD = Todo competidor (23+          **
    **  u23 = Sub 23 (20-21-22)            **
    **  u20 = sub 20 (18-19)               **
    **  u18 = sub 18 (16-17)               **
    **  u16 = sub 16 (14-15)               **
    *****************************************
"""

class ChampForm(forms.Form): 
    # ID	NOMBRE_CAMPEONATO	FECHA_INICIO	FECHA_TERMINO	REGION	PAIS	DIRECCION   NUMERO_ETAPAS
    # PK    event_name          init_date       finish_date     region  country direction   number_stages
    event_name = forms.CharField(label='Nombre del campeonato', max_length=50)
    #event_name = models.CharField(max_length=50, null=False, default='NOMBRE_CAMPEONATO') 
    limit_club = forms.IntegerField()
    #limit_club = models.IntegerField(choices=limit_club_choices, default=0)
    categorys = forms.CharField(label='Categoria',max_length=10)
    #category = models.CharField(max_length=8,default='00000000')
    region = forms.CharField(label='Region',max_length=20)
    #region = models.CharField(max_length=50, null=False, default='REGION')
    direction = forms.CharField(label='Dirección', max_length=20)
    #direction = models.CharField(max_length=50, null=False, default='DIRECCION')
    limit_athle = forms.IntegerField()
    #limit_athle = models.IntegerField(choices=limit_atle_choices, default=0)
    init_date = forms.DateTimeField(initial=datetime.datetime.today)
    #init_date = models.DateTimeField(default=timezone.now, null=False)
    finish_date = forms.DateTimeField(initial=datetime.datetime.today)
    #finish_date = models.DateTimeField(default=timezone.now, null=False)
    
    all_category =  ('SC','u16','u18','u20','u23','TD','CD','A','M','PREP')
    
    def __init__(self,data=None):
        if data:
            new_data = data.dict()
            if not new_data.get('atlexclub'):
                new_data['limit_club'] = 0
        
            new_data['init_date'] += 'T08:00:00-0000'
            new_data['finish_date'] +='T08:00:00-0000'

            categor = ''
            for x in self.all_category:
                if new_data.get(x):
                    new_data.pop(x)
                    categor +='1'
                else:
                    categor +='0'
            new_data['categorys'] = categor 
            data = new_data   
        super().__init__(data)

    def is_valid(self):
        return super().is_valid()   
    
    def is_valid_log(self):
        if self.is_valid():
            try:
                print('**Validando Formulario**')
                print('Campeonato:',self.data['event_name'])
                print('Inicio: %s | Fin: %s' % (self.data['init_date'],self.data['finish_date']))
                print('Direccion %s Region: %s' % (self.data['direction'],self.data['region']))
                print('Atletas por club: %s' % (self.data['limit_club']))
                print('Pruebas por atleta: %s' % (self.data['limit_athle']))
                print('Categorias %s:' % (self.data['categorys']))
            except Exception as e:
                print(e)
        else:
            print('formulario no valido')
    