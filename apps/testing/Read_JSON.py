import json
import os
from base.settings import BASE_DIR

def json_to_list(name): 
    fdir = os.path.join(BASE_DIR, 'json_files\\'+name)
    file = open(fdir,'r',encoding='utf-8')
    return json.load(file)
