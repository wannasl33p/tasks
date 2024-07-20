def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """
    parts = path.split('/')
    normalized_parts = []
    for part in parts:
        if part == '':
            continue
        elif part == '.':
            continue
        elif part == '..':
            if normalized_parts:
                normalized_parts.pop()
        else:
            normalized_parts.append(part)
    normalized_path = '/' + '/'.join(normalized_parts)

    return normalized_path
        
        
        
    


print(normalize_path("/bar"))
