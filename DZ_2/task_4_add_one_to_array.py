def add_one_to_array(digits):
    check_input_type(digits)
    check_len_list(digits)
    check_first_zero(digits)
    check_input_range(digits)

    digit = take_digit_from_array(digits)
    add = add_one(digit)

    return reverse_list(add)

def check_input_type(digits):
    if isinstance(digits,list):
        for digit in digits:
            if not isinstance(digit,int):
                raise TypeError('Значения в списке должны быть типа INT')
    else:
        raise TypeError('На вход должен подаваться список')
    return True

def check_len_list(digits):
    if len(digits) > 100 or len(digits) < 1:
        raise ValueError('Количество элементов в списке должно быть от 1 до 100')
    return True

def check_first_zero(digits):
    if digits[0] == 0:
        raise ValueError('Первый элемент не может быть 0')
    return True

def check_input_range(digits):
    for digit in digits:
        if digit not in range(0,10):
            raise ValueError('Значения в списке должны быть в диапазоне от 0 до 9')
    return True

def take_digit_from_array(digits):
    digit = 0
    for i in range(len(digits)):
        digit += digits[i]*10**(len(digits)-1-i)
    return digit

def reverse_list(array):
    reverse = []
    for i in range(-1,-len(array)-1,-1):
        reverse.append(array[i])
    return reverse

def add_one(digit):
    digit+=1
    add = []
    while digit > 0:
        add.append(digit % 10)
        digit //= 10
    return add

print(add_one_to_array([i for i in range(9,10)]*100))