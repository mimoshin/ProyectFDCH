from django.urls import path
from . import views
urlpatterns = [
    path('',views.principal,name='principal'),
    path('results',views.results_view,name='results_view'),
    path('load_results/<int:c_id>',views.load_results,name='ld_results'),
    path('delete_results/<int:c_id>',views.delete_results,name='dl_results'),
    path('athletes',views.athletes_view,name='athle_view')

]