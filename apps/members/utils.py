def max_pages(num,total):
    maxpages = int(num/total)+1
    return maxpages

def determinate_pages(num,total,present,action):
    max = max_pages(num,total)
    if action == 'next':
        if present == max:
            data = {'previous':present-1,'present':present,'next':max,'max':max} 
        else:
            data = {'previous':present,'present':present+1,'next':present+2,'max':max}

    elif action == 'prev':
        if present == 1:
            data = {'previous':1,'present':1,'next':2,'max':max}
        elif present == max:
            data = {'previous':present-2,'present':present-1,'next':max,'max':max} 
        else:
            data = {'previous':present-2,'present':present+1,'next':present+1,'max':max}
    return data
