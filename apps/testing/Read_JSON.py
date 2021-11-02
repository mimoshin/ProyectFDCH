import json

def json_to_list(name): 
    file = open('C:\\Users\\Franco\\Desktop\\Proyectos\\Fedachi\\Codigo\\files\\json_files\\'+name,'r',encoding='utf-8')
    #C:\Users\Franco\Desktop\Proyectos\Fedachi\Codigo\files\json_files
    return json.load(file)
