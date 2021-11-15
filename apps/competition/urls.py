from django.urls import path
from .views import (Qcompetitions, Qjumps, change_result, competitionView, download_file, download_startlist, genSeries, lanzV2, newCompetition, nuevoatleta, 
                    otroview, pdfView, probandoGET, resultsView, saltoV2, startView, startlistView, verAtleta)

urlpatterns = [
    path('cview/<int:cID>',competitionView,name='competition'),
    path('starlist/<int:comptID>',startlistView,name='startlistView'),
    path('results/<int:comptID>',resultsView,name='results_view'),
    path('new_competition/<int:stID>',newCompetition,name='newCompetition'),
    path('Q_competitions',Qcompetitions,name='Qcompetitions'),
    path('gen_series/<int:cID>',genSeries,name='genSeries'),
    path('s2/<int:comptID>',saltoV2,name='saltos2'),
    path('t2/<int:comptID>',lanzV2,name='lanz2'),
    path('download_file',download_file,name='download_file'),
    path('download_startlist/<int:Type>',download_startlist,name='download_startlist'),
    path('probando',startView.as_view(),name='probando'),
    path('prueba2',otroview.as_view(),name='prueba2'),
    path('Prueba3/<int:c_id>',pdfView,name='prueba3'),
    path('respuesta',probandoGET,name='probandoGet'),
    path('change',change_result,name='changeResult'),
    path('veratle/<int:id>',verAtleta,name='veratleta'),
    path('nuevoatleta',nuevoatleta,name='nuevoatle'),
    path('Q_jumps/<int:asID>',Qjumps,name='Qjumps')
]