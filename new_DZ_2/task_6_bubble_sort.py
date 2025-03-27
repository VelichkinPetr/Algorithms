def bubble_sort(array, key, order_by):
    '''

    Функция bubble_sort последовательно сравнивает значения соседних элементов и меняет числа местами,
    если предыдущее оказывается больше последующего.

    Таким образом элементы с большими значениями оказываются в конце списка, а с меньшими остаются в начале.

    :param array: неотсортированный массив
    :param key: направление сортировки (lambda x,y: x>y или lambda x,y: x<y)
    :param order_by: ключ сортировки (key = obj:obj.property - сортировка Объектов(obj) по общему Свойству(property))
    :return: ничего не возвращает

    Временная сложность:
    - Лучший: O(n)
    - Средний: O(n^2)
    - Худший: O(n^2)

    '''


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