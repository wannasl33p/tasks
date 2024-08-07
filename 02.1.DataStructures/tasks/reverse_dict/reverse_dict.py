import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    new_dict: dict[str, list[str]] = {}
    temp_list: list[str | int] = []

    for key, value in dct.items():
        if value in temp_list:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
        temp_list.append(value)
    return new_dict
