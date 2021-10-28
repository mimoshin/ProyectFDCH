from django.shortcuts import redirect, render
from championship.models import Championship_Interface, stage_interface, test, competition
from members.models import athlete, athlete_interface
# Create your views here.

data = [ 
        ['TORNEO CIERRE 1ER SEMESTRE','2021-06-19','2021-06-20'],
        ['SEGUNDO TORNEO PREPARATORIO REGIONAL BIOBIO','2021-06-04','2021-06-04'],
        ['TORNEO RETORNO A LAS PISTAS IV REGIÓN','2021-05-28','2021-05-28'],
        ['TORNEO PREPARATORIO REGIONAL ADRABB','2021-05-26','2021-05-26'],
        ['II TORNEO PREPARATORIO 2021','2021-05-07','2021-05-07'],
        ['TORNEO PREPARATORIO 2021','2021-04-30','2021-04-30'],
        ['CAMPEONATO NACIONAL ADULTO','2021-04-20','2021-04-21'],
        ['CAMPEONATO NACIONAL MARCHA EN RUTA - ARICA','2021-04-15','2021-04-15'],
        ['CAMPEONATO NACIONAL DE LANZAMIENTOS - TEMUCO','2021-03-19','2021-03-19'],
        ['CAMPEONATO NACIONAL DE FONDO Y MEDIO FONDO - CORONEL','2021-02-27','2021-02-28'],
        ['CAMPEONATO NACIONAL VELOCIDAD - SANTIAGO','2021-02-26','2021-02-27'],
        ['CAMPEONATO NACIONAL DE SALTOS - SAN FERNANDO','2021-02-26','2021-02-26'],
        ['CAMPEONATO NACIONAL DE CROSS COUNTRY 2021 - SAN JOSÉ DE LA MARIQUINA','2021-02-01','2021-02-01']
        ]

regiones = []
def stats_views(request):
    return render(request,'generators.html',{'data':'data','usr':''})

def generar_champs(request):
    for x in data:
        Championship_Interface.generator_champs(data)
    return redirect('stats')

def generar_etapas(request):
    name = {1:'Primera Etapa Mañana',2:'Segunda Etapa Tarde', 3:'Tercera Etapa Mañana',4:'Cuarta Etapa Tarde'}
    champs_list = Championship_Interface.get_all_championships()
    for data in champs_list:
        for num in range(1,5):
            print(name[num])
            stage_interface.generator_stages(data.id,num,name[num])
    return redirect('stats')
    
def generar_competencias(request):
    data = {'primera':[0,2,4,6],'segunda':[7,8,10,14],'tercera':[1,3,5,9,15],'cuarta':[10,11,12,13]}
    compt_list = []
    for tests in test.objects.all():
        compt_list.append(tests)
    champs_list = Championship_Interface.get_all_championships()
    for campeonato in champs_list:
        stages_list = campeonato.stage_set.all()
        for etapa in stages_list:
            if etapa.stage_num == 1:
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][0]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][0]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][1]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][1]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][2]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][2]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][3]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['primera'][3]], 'DAMAS')
            
            elif etapa.stage_num == 2:
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][0]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][0]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][1]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][1]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][2]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][2]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][3]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['segunda'][3]], 'DAMAS')
           
            elif etapa.stage_num == 3:
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][0]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][0]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][1]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][1]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][2]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][2]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][3]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][3]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][4]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['tercera'][4]], 'DAMAS')
               
               
            elif etapa.stage_num == 4:
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][0]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][0]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][1]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][1]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][2]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][3]], 'DAMAS')
                
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][3]], 'VARONES')
                stage_interface.generator_compts(etapa.id, compt_list[data['cuarta'][3]], 'DAMAS')
    return redirect('stats')

    
def inscribir_enmasa(request):
    male_athlete = []
    female_athlete = []
    male_compt = []
    female_compt = []

    for athletes in athlete.objects.filter(gender='MASCULINO'):
        male_athlete.append(athletes)
    
    for athletes in athlete.objects.filter(gender='FEMENINO'):
        female_athlete.append(athletes)

    for compet in competition.objects.filter(gender='VARONES'):
        male_compt.append(compet)
    
    for compet in competition.objects.filter(gender='DAMAS'):
        female_compt.append(compet)

    a_mal_max = len(male_athlete)
    a_fem_max= len(female_athlete)
    c_mal_max = len(male_compt)
    c_fem_max= len(female_compt)
    
    ccm_count = 0
    ccf_count = 0
    print(a_mal_max,a_fem_max,c_mal_max,c_fem_max)
    
    #male
    #for x in range(c_mal_max):
     #   for a in male_athlete:
      #      if male_compt[x].inscription_set.count() < 30:
       #         stage_interface.new_inscription(a.id,male_compt[x].id)
        #    else:
         #       pass

    #female
    for x in range(c_fem_max):
        for a in female_athlete:
            if female_compt[x].inscription_set.count() < 30:
                stage_interface.new_inscription(a.id,female_compt[x].id)
            else:
                pass
            
    return redirect('stats')
        

"""
#male
females = athlete.objects.filter(gender='FEMENINO')
    for x in females:
        x.delete()

    for a in male_athlete:
        for x in range(ccm_count,ccm_count+3):
            if ccm_count< c_mal_max:
                ccm_count+=1
                if male_compt[x].inscription_set.count() < 30:
                    stage_interface.new_inscription(a.id,male_compt[x].id)
                else:
                    pass
                #print(male_compt[x].inscription_set.count())
                #stage_interface.new_inscription(a.id,male_compt[x].id)
                #print(a.first_name,male_compt[x],a.gender)
            else:
                pass
#female
    for a in female_athlete:
        for x in range(ccf_count,ccf_count+3):
            if ccf_count< c_fem_max:
                ccf_count+=1
                if female_compt[x].inscription_set.count() < 30:
                    stage_interface.new_inscription(a.id,female_compt[x].id)
                #stage_interface.new_inscription(a.id,female_compt[x].id)
                #print(a.first_name,female_compt[x],a.gender)
                else:
                        pass
"""