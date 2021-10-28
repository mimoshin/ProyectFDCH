from django.urls import path
from . import views

urlpatterns = [
    #path('',views.init_view,name='principal'),
    path('',views.championship_view,name='championships'),
    path('new',views.new_championship,name='new_champ'),
    path('review/<int:c_id>',views.review_championship,name='review_champ'),
    path('generador',views.generate_activitys,name='new_a'),
    path('new_compt/<int:stage_id>',views.new_competition,name='new_compt'),
    path('competition/<int:c_id>',views.review_competition,name='review_competition'),
    path('genA',views.generate_activitys,name='genActivitis'),
]