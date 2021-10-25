from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.principal_view,name='compt_principal'),
    path('load_sports',views.load_sports,name='ld_sports'),
    path('delete_sports',views.delete_sports,name='del_sports'),
    path('load_competitions',views.load_competitions,name='ld_competitions'),
    path('delete_competitions',views.delete_competitions,name='del_competitions'),
    path('track',views.track_principal,name='track_principal'),
    path('load_th2s',views.load_trackhead2s,name='ld_th2s'),
    path('delete_th2s',views.delete_trackhead2s,name='del_th2s'),
    path('load_track2s',views.load_track2s,name='ld_track2s'),
    path('delete_track2s',views.delete_track2s,name='del_track2s'),
    path('load_resume',views.load_resume,name='ld_resume'),
    path('delete_resume',views.delete_resume,name='del_resume'),
    path('resume_throw',views.load_resume_trhow,name='load_RMT'),
    path('del_resumeT',views.delete_resume_trhow,name='del_RMT'),
    path('resume_jump',views.load_resume_jump,name='load_RMJ'),
    path('del_resumeJ',views.delete_resume_jump,name='del_RMJ'),
    path('compare',views.compare,name='ncompare'),
    path('throw',views.throw_principal,name='throw_principal'),
    path('jump',views.jump_principal,name='jump_principal'),
    path('viewR/<int:compt>',views.view_results,name='view_results'),
]