def recursive_max(array):
    if array == '':
        raise TypeError
    elif array == []:
        return 0
    elif len(array) == 1 and array[0] == '':
        raise TypeError

    elif len(array) == 1:
        return array[0]
    rec = recursive_max(array[1:])

    return array[0] if array[0] >= rec else rec
