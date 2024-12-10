
def bubble_sort(array, key, order_by):
    check_input_type(array)

    lenght = len(array)
    if lenght == 0: return []

    for i in range(0, lenght, 1):
        for j in range(0, lenght - 1 - i, 1):
            if order_by( key(array[j]), key(array[j + 1]) ):
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    if not isinstance(array[0], int):
        return [any.age for any in array]
    return array

def check_input_type(array):
    if not isinstance(array,list):
        raise TypeError('На вход должен подаваться список')
    for elem in array:
        if isinstance(elem, str):
            raise TypeError('Значения в списке должны быть типа INT')
    return True

