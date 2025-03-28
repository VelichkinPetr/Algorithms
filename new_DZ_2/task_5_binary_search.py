def search_binary(arr: list[int], target):
    '''

            >>Бинарный поиск<<

    Бинарный поиск работает следующим образом:
        1. Определяется средний элемент массива.
        2. Если искомое значение равно среднему, поиск завершается.
        3. Если искомое значение меньше среднего, поиск продолжается в левой половине,
        иначе — в правой.
        4. Процесс повторяется до нахождения элемента или определения его отсутствия.

    :param arr: отсортированный список
    :param target: искомый элемент
    :return: индекс найденного элемента или -1, если элемент не найден

    Временная сложность:
    - Лучший: O(log n)
    - Средний: O(log n)
    - Худший: O(log n)

    '''


    if not isinstance(arr, list): raise TypeError #Валидация списка
    if not isinstance(target, int): raise TypeError #Валидация искомого элемента

    mid = len(arr) // 2

    if mid == 0 and arr[mid] != target: return -1 #Выход за левую границу списка
    if target > arr[-1]: return -1 #Выход за правую границу списка

    if arr[mid] == target: # Искомый элемент в середине списка
        return mid

    if arr[mid] > target: # Искомый элемент слева от середины списка
        return search_binary(arr[:mid], target)

    if arr[len(arr) // 2] < target: # Искомый элемент справа от середины списка
        return mid + search_binary(arr[mid:], target)

