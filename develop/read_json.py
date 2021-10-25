import json

def json_to_list(name): 
    file = open("C:\\Users\\Franco\\Desktop\\Proyectos\\Fedachi\\Codigo\\files\\json_files\\"+name,'r',encoding='utf-8')
    return json.load(file)

def write_json(data,name):
    file = open("C:\\Users\\Franco\\Desktop\\Proyectos\\Fedachi\\Codigo\\files\\json_files\\Archivos corregidos\\"+name,'w+',encoding='utf-8')
    json.dump(data,file, indent=4, ensure_ascii=False) 