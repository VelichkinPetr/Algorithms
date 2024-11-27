def fibonacci(n):
    try:
        check_input_type(n) #1
        check_input_range(n) #1
    except TypeError:
        return []
    except ValueError:
        return []
    return rezult(n) # 1 or 3+(n-2)*4 = n

def check_input_type(n):
    if not isinstance(n, int): #1
        raise TypeError('Значение должны быть типа INT')
    return True

def check_input_range(n):
    if n < 0: #1
        raise ValueError('Значение должны быть положительным')
    return True

def rezult(n):
    if n == 0: #1
        return [0]
    elif n == 1: #1
        return [0,1]
    else:
        elem_1 = 1 #1
        elem_2 = 1 #1
        list_fib = [0,elem_1,elem_2] #1
        for i in range(2, n):# n-1
            elem_1, elem_2 = elem_2, elem_1 + elem_2 #3
            list_fib.append(elem_2) #1
        return list_fib

# 1+1+n = 2+n = O(n) - линейная сложность
