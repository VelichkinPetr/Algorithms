def recursive_sum_even(array):
    if array == []:
        return 0
    array[0] = array[0] if array[0] % 2 == 0 else 0
    if len(array) == 1:
        return array[0]
    rec = recursive_sum_even(array[1:])
    return array[0]+ rec


print(recursive_sum_even([]))
