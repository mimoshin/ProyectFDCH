from django.urls import path
from .views import logView,logoutView
urlpatterns = [
    path('',logView,name='login'),
    path('logout',logoutView,name='logout')
]