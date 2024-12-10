import random


def selection_sort_and_count_operations(array,order_by):
    check_input_type(array)
    count_exchanging_elements = 0
    count_comparisons_elements = 0

    for i in range(0,len(array)-1,1):
        iminimum = i

        for j in range(i,len(array),1):
            if order_by(array[iminimum], array[j]):
                count_comparisons_elements +=1
                iminimum = j
        buff = array[i]
        array[i] = array[iminimum]
        array[iminimum] = buff
        count_exchanging_elements += 1
    return array,count_comparisons_elements,count_exchanging_elements


def check_input_type(array):
    if not isinstance(array,list):
        raise TypeError('На вход должен подаваться список')
    for elem in array:
        if not isinstance(elem, int):
            raise TypeError('Значения в списке должны быть типа INT')
    return True


