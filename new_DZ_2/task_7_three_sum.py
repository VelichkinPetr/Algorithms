def three_sum(arr: list[int]):

    '''

    Функцию three_sum(arr), находит все уникальные тройки элементов, сумма которых равна 0

    :param arr: список чисел
    :return: список списков

    Временная сложность:
    - Лучший: O(n^2)
    - Средний: O(n^2)
    - Худший: O(n^2)

    '''

    arr.sort()

    three_list = []
    for i in range(len(arr)):
        for j in range(i,len(arr)-1):
            if arr[i] + arr[i+1] + arr[j+1] == 0 and [arr[i], arr[i+1], arr[j+1]] not in three_list:
                three_list.append([arr[i], arr[i+1], arr[j+1]])

    return three_list