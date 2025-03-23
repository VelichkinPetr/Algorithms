def  fast_power(a:float, n:int) -> float:
    """

    Функция, которая вычисляет a^n, с использованием алгоритма быстрого возведения в степень
    (метод бинарного разложения показателя)

    :param a: int
    :param n: int
    :return: float

    Временная сложность: O(log n)
    """
    if n < 0:
        return fast_power(1 / a, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_power(a ** 2, n / 2)
    else:
        return a * fast_power(a ** 2, (n - 1) / 2)
