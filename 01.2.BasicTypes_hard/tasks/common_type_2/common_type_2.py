import typing as tp


def convert_to_common_type(data: list[tp.Any]) -> list[tp.Any]:
    """
    Takes list of multiple types' elements and convert each element to common type according to given rules
    :param data: list of multiple types' elements
    :return: list with elements converted to common type
    """
    my_list=[]
    list_for_return =[]
    for values in data :
        if bool(values):
            my_list.append(type(values)) 

     
    if list in my_list or tuple in my_list :
        for value in data :
            if type(value) is not list and bool(value) and type(value) is not tuple :
                list_for_return.append([value])
            elif type(value) is tuple and bool(value):
                list_for_return.append(list(value))
            elif bool(value) :
                list_for_return.append(value)
            else :
                list_for_return.append([])              
        return list_for_return
        
    elif str in my_list :
        return [str(value) if bool(value) else '' for value in data]
    
    elif int in my_list or float in my_list :
        if float in my_list :
            return [float(value) if bool(value) else 0.0 for value in data]
        else :
            if 1 not in data and 0 not in data :
                return [value if bool(value) else 0 for value in data]
            else :
                return [bool(value) if bool(value) else False for value in data]  
    elif bool in my_list :
        return [bool(value) if bool(value) else False for value in data]
    
    else :
        if 0 in data :
            if None not in data :
                return [int(value) for value in data]
            else :
                for value in data :
                    if value != None and value != "" :
                        list_for_return.append(int(value))
                    else:
                        list_for_return.append(0)
                return list_for_return
            
        elif '' in data or None in data :
            return ['' for value in data]
        elif False in data :
            return [bool(value) for value in data] 
        
    
    
print(convert_to_common_type([False, False, False]))



