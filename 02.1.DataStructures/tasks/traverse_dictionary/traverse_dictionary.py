import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result: list[tuple[str, any]] = []

    for key, value in dct.items():
        current_key = f"{prefix}.{key}" if prefix else key
        if type(value)==dict:
            result.extend(traverse_dictionary_immutable(value, current_key))
        else:
            result.append((current_key, value))

    return result


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for key , value in dct.items() :
        current_key = f"{prefix}.{key}" if prefix else key
        if type(value)==dict:
            result.extend(traverse_dictionary_immutable(value, current_key))
        else:
            result.append((current_key, value))


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    
    result: list[tuple[str, int]] = []
    queue = [(key, value) for key, value in dct.items()]

    while queue:
        key, value = queue.pop(0)
        if type(value)==dict:
            for inner_key, inner_value in value.items():
                queue.append((f"{key}.{inner_key}", inner_value))
        else:
            result.append((key, value))

    return result
                
            
            
        
            
                
            
    
    
    
    
d = {
    "a": 1,
    "b": {
        "c": 2,
        "d": 4
    }
}
print(traverse_dictionary_iterative(dct=d))

