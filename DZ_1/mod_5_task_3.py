def count_ones(n):
    check_input_type(n)#1
    check_input_range(n)#1
    return rezult(n) #2 + log n * 3


def check_input_type(n):
    if not isinstance(n, int): #1
        raise TypeError('Значение должны быть типа INT')
    return True

def check_input_range(n):
    if n < 0: #1
        raise ValueError('Значение должны быть положительным')
    return True

def rezult(n):
    if n > 0: #1

        count = 0 #1
        while n != 1: #log n -1
            if n % 2 != 0: #1
                count += 1 #1
            n = n//2 #1
        return count+1

    else:
        return 0
# 1 + 1 + 2 + (log n -1) * 3  = 3log n + 1 = O(log n) - логорифмическая сложность