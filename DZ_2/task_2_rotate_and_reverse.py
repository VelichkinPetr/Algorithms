def rotate_and_reverse(arr, k):
    check_input_type(arr)
    check_empty_list(arr)
    check_k(k)
    return get_formatted_list(arr, k)


def check_input_type(array):
    if not isinstance(array,list):
        raise TypeError('На вход должен подаваться список')
    return True

def check_k(k):
    if not isinstance(k, int):
        raise TypeError('Значение сдвига должны быть типа INT')
    elif k < 0:
        raise ValueError('Значение сдвига должны быть положительным')
    return True

def check_empty_list(array):
    if len(array) == 0:
        raise ValueError('Список не должен быть пуст')
    return True

def get_formatted_list(array, k):
    n = len(array)
    if k > n:
        k %= n

    x = array[-k:]
    for i in range(-1, -n, -1):
        if i >= -n + k:
            array[i] = array[i - k]

    for j in range(-k, 0, 1):
        array[-n - j - 1] = x[-j - 1]

    for i in range(n // 2):
        buff = array[i]
        array[i] = array[-i - 1]
        array[-i - 1] = buff

    return array
