def factorial(n:int) -> int:
    try:
        check_input_type(n) #1
        check_input_range(n) #1
    except TypeError:
        return 0
    except ValueError:
        return 0
    return rezult(n) #1 or (1+n*1) = 1 or (1+n) = n

def check_input_type(n):
    if not isinstance(n, int): #1
        raise TypeError('Значение должны быть типа INT')
    return True

def check_input_range(n):
    if n < 0 or n > 20: #1
        raise ValueError('Значение должны быть положительным не большим 20')
    return True

def rezult(n):
    if n == 0: #1
        return 1
    else:
        fact = 1 #1
        for i in range(1, n + 1): #n
            fact *= i #1
        return fact

# 1+1+1+n = 3+n = O(n) - линейная сложность
