from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal_view,name='principal_view'),
    path('fonts',views.get_fonts,name='get_fonts')
]