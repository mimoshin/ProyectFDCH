from django.urls import path
from . import views

urlpatterns = [
    path('',views.init_view,name='principal'),
    path('login',views.login_view,name='login'),
    path('logout',views.user_logout,name='logout'),
]