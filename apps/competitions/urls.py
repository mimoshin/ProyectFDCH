from django.urls import path
from . import views

urlpatterns = [
    path('starlist/<int:cp_id>', views.starlist_view,name='starlist_view'),
    path('results/<int:cp_id>', views.results_view,name='results_view'),
    path('download_file',views.download_file,name='download_file'),
    path('download_startlist/<int:Type>',views.download_startlist,name='download_startlist'),
    path('download_results/<int:Type>',views.download_results,name='download_results'),
    path('probando',views.startView.as_view(),name='probando'),
    path('prueba2',views.otroview.as_view(),name='prueba2'),
    path('Prueba3/<int:c_id>',views.pdfView,name='prueba3'),
]