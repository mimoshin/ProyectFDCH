RUT_TUPLE = (48,49,50,51,52,53,54,55,56,57,75,107)

def null_wrong(text):
    spliter = text.split(' ')
    if '' in spliter:
        return True

def tab_wrong(text):
    spliter = text.split(' ')
    if '\t' in spliter:
        return True
    else:
        for x in spliter:
            for i in x:
                if ord(i) == 9:
                    return True

def delete_trashstr(data):
    if isinstance(data,str):
        if '\t' in data:
            aux2 = [data]
            #print("tabulacion webiando",aux2)
            aux = delete_trashlist(data.split('\t'))
            if len(aux) >1:
                #print(aux, len(aux))
                name = ''
                for x in aux:
                    name+=x+' '
                name = name.strip()
                return name, True
               
            else:
                return data.strip(),False
        else:
            return data.strip(),False

def delete_trashlist(data):
    if isinstance(data,list):
        if '' in data:
            #print('si hay vacio')
            data.pop(data.index(''))
            return delete_trashlist(data)
        elif ' ' in data:
            #print('si hay espacio')
            data.pop(data.index(' '))
            return delete_trashlist(data)
        elif '\t' in data:
            #print('si hay tabulacion')
            data.pop(data.index('\t'))
            return delete_trashlist(data)
        else:
            for x in data:
                index = data.index(x)
                retorno = delete_trashstr(x)
                #if retorno[1]:
                    #print("retorno",retorno)
                data[index] = retorno[0]
                #print(data[index])
            return data

def repair_trash(text_list):
    text = ''
    for i in text_list:
        text += i +' '
    text = text[:-1]
    return text

def repair_rut(rut):
    aux = rut
    for x in rut:
        if rut == 'Nulo':
            pass
        elif ord(x) == 46:
            rut = rut.replace('.','')
        elif ord(x) == 45:
             rut = rut.replace('-','')
        elif ord(x) == 32:
            rut = rut.replace(' ','')
        elif ord(x) not in RUT_TUPLE:
            index = ord(x)
            char = chr(index)
            new = rut.replace(char,'') 
            rut = new
    print("antes:",aux,len(aux)," | despues:",rut,len(rut))
    return rut
    
def detect_dg(rut):
    large = len(rut)
    index = rut.find('-')
    if large ==11:
        print("rut de 11",rut)
    if index != -1:
        if large > index:
            #print("si tiene digito verificador",rut)
            return 1
        else:
            print("no tiene digito verificador",rut)
    elif index == -1:
        return 0
    
def detect_fail_rut(rut):
    if rut[-1] == '0' and rut[-2] == '.':
        repair_rut(rut[:-1])
        return 1
    else:
        return 0
