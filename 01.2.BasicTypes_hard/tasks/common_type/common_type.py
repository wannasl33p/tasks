def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
    if type1 == str or type2 == str:
        return str
    if type1==list or type2==list:
        if type1==tuple or type2==tuple :
            return list
        elif type1==range or type2==range:
            return list
        elif type1==list and type2==list:
            return list
        elif type1==int or type2==int :
            return str
        elif type1==complex or type2 ==complex :
            return str
        elif type1==float or type2==float:
            return str
        elif type1==bool or type2==bool :
            return str
    if type1==tuple or type2==tuple :
        if type1==tuple and type2==tuple :
            return tuple 
        elif type1==range or type2==range:
            return tuple 
        elif type1==int or type2==int :
            return str
        elif type1==complex or type2 ==complex :
            return str
        elif type1==float or type2==float:
            return str
        elif type1==bool or type2==bool :
            return str
    if type1==range or type2==range :
        if type1==range and type2 ==range :
            return tuple
        elif type1==int or type2==int :
            return str
        elif type1==complex or type2 ==complex :
            return str
        elif type1==float or type2==float:
            return str
        elif type1==bool or type2==bool :
            return str
    if type1==bool or type2==bool :
        if type1==bool and type1==bool :
            return bool
        elif type1==int or type2==int :
            return int
        elif type1==complex or type2==complex :
            return complex
        elif type1==float or type2==float :
            return float
    if type1==float or type2==float :
        if type1==int or type2==int :
            return float
        elif type1== float and type2==float :
            return float
        elif type1==complex or type2==complex :
            return float
    if type1==int or type2==int:
        if type1==int and type2==int :
            return int
        elif type1==complex or type2==complex:
            return int
    if type1==complex and type2==complex :
        return complex
    
        
        
    
    