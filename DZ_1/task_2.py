def min_frequent_elem(numbers:list[int]) -> int:
    try:
        check_input_type(numbers)
        check_empty_input(numbers)
        check_len_list(numbers)
        check_input_range(numbers)
    except TypeError:
        return []
    except ValueError:
        return []
    rezult = get_min_common_elem(numbers)
    return rezult

def check_empty_input(numbers):
    if numbers == []:
        raise ValueError('Входные данные не могут быть пустым списком')

def check_input_type(numbers):
    if isinstance(numbers,list):
        for number in numbers:
            if not isinstance(number,int):
                raise TypeError('Значения в списке должны быть типа INT')
    return True
def check_len_list(numbers):
    if len(numbers) > 10**5:
        raise ValueError('Максимальное количество элементов в списке = 10^5')
    return True

def check_input_range(numbers):
    for number in numbers:
        if number not in range(1,2*10**4+1):
            raise ValueError('Значения в списке должны быть в диапазоне от 1 до 2*10^4')
    return True

def get_min_common_elem(numbers):
    min_elem = 0
    count_elem = 0
    for number in numbers:
        if numbers.count(number) > count_elem:
            min_elem = number
            count_elem = numbers.count(number)
        elif numbers.count(number) == count_elem and number < min_elem:
            min_elem = number
    return min_elem