def sum_even_numbers_in_list(numbers:list[int]) -> int:

    check_input_type(numbers)
    check_len_list(numbers)
    check_input_range(numbers)

    sum = sum_even(numbers)
    sum = check_negative_sum(sum)
    return sum

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
        if number not in range(-2*10**4,2*10**4+1):
            raise ValueError('Значения в списке должны быть в диапазоне от -2*10^4 до 2*10^4')
    return True

def sum_even(numbers):
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
    return sum

def check_negative_sum(sum):
    if sum < 0:
        sum = 1
    return sum


