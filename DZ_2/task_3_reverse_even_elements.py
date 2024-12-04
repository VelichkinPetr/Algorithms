def reverse_even_elements(arr):
    check_input_type(arr)
    check_empty_list(arr)
    return get_formatted_list(arr)

def check_input_type(array):
    if not isinstance(array,list):
        raise TypeError('На вход должен подаваться список')
    for elem in array:
        if not isinstance(elem, int):
            raise TypeError('Значения в списке должны быть типа INT')
    return True

def check_empty_list(array):
    if len(array) == 0:
        raise ValueError('Список не должен быть пуст')
    return True

def get_list_index_even_elem(array):
    index_even_list = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            index_even_list.append(i)
    return index_even_list

def reverse_list(array):
    reverse = []
    for i in range(-1,-len(array)-1,-1):
        reverse.append(array[i])
    return reverse

def get_formatted_list(array):
    index_even_list = get_list_index_even_elem(array)
    reverse_even_list = reverse_list(index_even_list)
    for i in range(len(index_even_list)//2):
        buff = array[index_even_list[i]]
        array[index_even_list[i]] = array[reverse_even_list[i]]
        array[reverse_even_list[i]] = buff
    return array

