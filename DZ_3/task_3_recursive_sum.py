def recursive_sum(array):
    if array == []:
        return 0
    return array[0]+recursive_sum(array[1:])

