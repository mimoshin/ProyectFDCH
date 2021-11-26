import json
import os
import pytz
from .settings import BASE_DIR
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
import datetime

def json_to_list(name):
    file_dir = os.path.join(BASE_DIR,'json_files\\'+name)
    file = open(file_dir,'r',encoding='utf-8')
    return json.load(file)


def Qlog_user(user):
    if user == AnonymousUser():
        return False
    else:
        return True

def str_to_DateTimeField(time):
    stgo_tz = pytz.timezone('America/Santiago') 
    aux = time.split(' ')
    a_date, a_time = aux[0].split('-'), aux[1].split(':')
    year,month,day = int(a_date[0]), int(a_date[1]), int(a_date[2])
    hour,minute,second =int(a_time[0]), int(a_time[1]), int(a_time[2]) 
    datetime.datetime.now(tz=timezone.utc)
    datetime_field = datetime.datetime(year,month,day,hour,minute,second,tzinfo=stgo_tz)
    return datetime_field