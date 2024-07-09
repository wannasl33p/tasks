def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """
    start_path=path

    for i in range(len(path)):
        if i+1<len(path) and path[i]=='.'  and path[i+1]=='.' and len(path[i+2:])!=0 :
            if path[i+2:]!='/':
                    path=path[i+2:]
    while '//' in path :
        path=path.replace('//','/')
    if len(path)!=1 and '.' in path:
        path=path.replace('.', '')
    
        
        
    return path
            



print(normalize_path("./bar"))
