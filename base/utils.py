import os 
from .settings import FONTS_DIR
from django.contrib.auth.models import AnonymousUser

def get_fonts():
    return os.listdir(FONTS_DIR)

def Qlog_user(user):
    if user == AnonymousUser():
        return False
    else:
        return True
