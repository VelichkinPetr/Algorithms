def is_palindrome(x):
    check_input_type(x)#1
    return polindrome(x,len_int(x))

def check_input_type(x):
    if not isinstance(x, int): #1
        raise TypeError('Значение должны быть типа INT')
    return True

#def check_input_range(x):
#    if x <= -231 or x >= 231: #1
#        raise ValueError('Значение должны быть от -231 до 231')
#   return True

def len_int(x):
    len = 0#1
    while x not in [-1,0]: #n
        len += 1 #1
        x = x // 10 #1
    return len

def polindrome(x,len_int):
    for i in range(1,len_int//2+1): #1,2 #n//2+1
        if x%10 == x//10**(len_int-i):
            x = (x%10**(len_int-i))//10 #5
            len_int -=1 #2
        else:
            return False
    return True
# 1 + 1 + 2n + 7*(n//2 + 1) = 2 + 2n + 3,5n + 7 = 5,5n + 9 = O(n) - линейная сложность
