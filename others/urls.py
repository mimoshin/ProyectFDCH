from django.urls import path
from . import views
urlpatterns = [
    path('',views.principal_view,name='other_principal'),
    path('load_categories',views.load_categories,name='ld_categories'),
    path('delete_categories',views.delete_categories,name='del_categories'),
    path('load_sexes',views.load_sexes,name='ld_sexes'),
    path('delete_sexes',views.delete_sexes,name='del_sexes'),
]