import math

def max_in_range(arr:list, start:int, end:int) -> list[int]:
    check_input_type(arr)
    check_start_end_type(start,end)
    check_input_range(arr, start, end)
    return take_max_elem(arr,start,end)

def check_input_type(array):
    if isinstance(array,list):
        for number in array:
            if not isinstance(number,int):
                raise TypeError('Значения в списке должны быть типа INT')
    return True

def check_start_end_type(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError('Границы поиска должны быть типа INT')
    return True

def take_max_elem(list,start,end):
    max_elem = -math.inf
    index_relative = -1
    for i in range(start,end+1):
        if list[i] > max_elem:
            max_elem = list[i]
            index_relative = i-start
    index_absolute = index_relative + start
    return max_elem,index_absolute,index_relative

def check_input_range(list,start,end):
    if len(list) == 0:
        raise ValueError('Список не должен быть пуст')
    elif len(list)-1 < end or len(list)-1 < start:
        raise ValueError('Длина списка должна быть больше правой границы интервала поиска')
    elif start < 0 or end < 0:
        raise ValueError('Индекс должен быть положительным целым числом')
    elif start > end:
        raise ValueError('START должен быть больше END')

