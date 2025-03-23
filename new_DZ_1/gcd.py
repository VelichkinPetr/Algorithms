def  gcd(a:int, b:int) -> int:
    """

    Функция, которая принимает два целых числа и возвращает их наибольший общий делитель,
    используя алгоритм Евклида

    :param a: int
    :param b: int
    :return: int

    Временная сложность: O( log min(a,b) )
    """
    print(a,b)
    if b==0:
        return abs(a)
    return gcd(b,a%b)
