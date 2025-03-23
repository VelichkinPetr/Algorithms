from math import floor,sqrt

def  is_prime(n:int) -> bool:
    """

    Функция, которая принимает целое число n и возвращает true,
    если число является простым, и false в противном случае.

    :param n: int
    :return: bool

    Временная сложность: O(sqrt (n))
    """
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3,floor(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True
