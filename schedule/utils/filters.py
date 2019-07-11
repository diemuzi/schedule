def isdefined(string):
    """
    Check if value has data

    Will return True if data exists, else False

    :param dict|list|str|int|float|None string: Data to test with

    :return: bool
    """

    if string is None:
        return False
    elif type(string) is str and not string.strip():
        return False
    elif type(string) is str and string == '':
        return False
    elif type(string) is int and not string:
        return False
    elif type(string) is float and not string:
        return False
    elif type(string) is list and len(string) == 0:
        return False
    elif type(string) is dict and len(string) == 0:
        return False
    elif type(string) is bool:
        return True
    else:
        return True
