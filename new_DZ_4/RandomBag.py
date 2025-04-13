from random import randint

class RandomBag:

    def __init__(self, size = None, RB = None):

        if isinstance(RB, RandomBag):
            self._size = RB._size
            self._count = 0
            self._array = RB._array
        else:
            self._size = size or 5
            self._count = 0
            self._array = [None] * self._size

    def __memory_alloc(self):

        self._size = self._size + 1 + self._size // 2
        new_memory = [None] * self._size
        for i, elem in enumerate(self._array):
            new_memory[i] = elem

        return new_memory

    def get(self):
        return self._size, self._array,self._count

    def add(self, item: any) -> None:
        """

        Добавить элемент в конец массива.
        При достижении предела count == size происходит расширение внутреннего массива
        (например, увеличение в 2 раза).

        :param item: значение элемента
        :return: None

        """
        if self._count == self._size:
            self._array = self.__memory_alloc()

        self._array[self._count] = item
        self._count += 1

    def get_random(self) -> any:
        """

        Возвращает случайный элемент из мешка без его удаления.
        Для реализации можно использовать выбор случайного индекса в диапазоне [0, count – 1].

        :return: значение случайного элемента

        """
        if self._count == 0:
            raise ValueError

        random_index = randint(0, self._count-1)
        return self._array[random_index]

    def contains(self, item: any) -> bool:
        '''

        Проверяет наличие указанного элемента в мешке.
        Если элемент найден, возвращает True, иначе – False.

        :param item: значение элемента
        :return: True or False

        '''

        item_find = False

        for i in range(self._count):
            if self._array[i] == item:
                item_find = True

        return item_find

    def remove_random(self) -> any:
        '''

        Удалить и вернуть случайный элемент. Для этого
        выбирается случайный индекс, по которому элемент удаляется (например,
        заменой последним элементом для оптимизации или выполнением сдвига
        оставшихся элементов). В случае, если мешок пуст, необходимо породить
        исключение (например, ValueError).

        :return: значение случайного элемента

        '''
        if self._count == 0:
            raise ValueError

        random_index = randint(0, self._count-1)
        buff = self._array[random_index]

        for i in range(-self._size + random_index, -self._size + self._count, 1):

            if i == -1:
                self._array[i] = None
            else:
                self._array[i] = self._array[i+1]

        self._count -=1

        return buff

    def count_item(self, item: any) -> int:
        '''

        Возвращает число вхождений указанного элемента в
        RandomBag. Для этого необходимо перебрать все элементы (с индексами от 0
        до count – 1) и подсчитать количество повторов.

        :param item: элемент
        :return: int
        '''

        count_value = 0

        for elem in self._array:
            if elem == item:
                count_value += 1

        return count_value

    def replace_random(self, new_item: any) -> any:
        '''

        Заменить случайно выбранный элемент в мешке
        на новый new_item. Метод возвращает старое значение элемента. Если мешок
        пуст, необходимо породить исключение.

        :param new_item: значение нового элемента
        :return: значение старого элемента

        '''

        if self._count == 0:
            raise ValueError

        random_index = randint(0,self._count-1)
        data = self._array[random_index]
        self._array[random_index] = new_item

        return data

    def remove_all(self, item: any) -> int:
        '''

        Удалить все вхождения указанного элемента из RandomBag.
        Метод возвращает количество удаленных элементов.

        :param item: значение удаляемого элемента
        :return: количество удаленных элементов

        '''


        if self.count_item(item) == 0:
            return 0

        count_elem = 0
        k = 0

        for j in range(self._count):
            if self._array[k] == item:

                for i in range(-self._size+k, -self._size + self._count, 1):
                    if i == -1:
                        self._array[i] = None
                    else:
                        self._array[i] = self._array[i + 1]

                count_elem += 1

            else:
                k+=1

        self._count -= count_elem

        return count_elem

