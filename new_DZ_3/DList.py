class DList:

    def __init__(self):

        self.__size = 1
        self.__count = 0
        self.__memory = [None] * self.__size

    def get_memory(self) -> list: return self.__memory

    def set_memory(self, memory: list):
        self.__size = len(memory)
        self.__memory = memory
        self.__count = self.__size - self.__memory.count(None)


    def __str__(self):

        array_out = []
        for elem in self.__memory:
            if elem != None:
                array_out.append(elem)

        return f'{array_out}'

    def __memory_allocation(self) -> list:
        '''

        Функция выделения памяти. При переполнении старой памяти,
        выделяет новый кусок и копирует содержимое старого массива в новый.

        :return: новый список из None

        '''

        self.__size = self.__size + 1 + self.__size // 2
        new_memory = [None] * self.__size

        for i, elem in enumerate(self.__memory):
            new_memory[i] = elem

        return new_memory

    def add(self,item: any) -> None:
        '''

        Фунция добавления элемента в конец массива.

        :param item: значение элемента
        :return: None

        Временная сложность:
        Лучший: О(1)
        Средний: О(1)
        Худший: О(n)

        '''

        if self.__count == self.__size:
            new_memory = self.__memory_allocation()
            self.__memory = new_memory

        self.__memory[self.__count] = item
        self.__count += 1

    def add_front(self,item: any) -> None:
        '''

        Фунция добавления элемента в начало массива.

        :param item: значение элемента
        :return: None

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''
        if self.__count == self.__size:
            new_array = self.__memory_allocation()
            self.__memory = new_array

        for i in range(0, self.__count, 1):
            buff = self.__memory[self.__count - 1 - i]
            self.__memory[self.__count - i] = buff

        self.__memory[0] = item
        self.__count += 1

    def find(self,item: any) -> int or -1:
        '''

        Функция поиска индекса элемента по его значению.

        :param item: искомое значение
        :return: индекс или -1

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''

        for index, elem in enumerate(self.__memory):
            if elem == item:
                return index
        return -1

    def __index(self,item: any) -> int or ValueError:

        '''

        Вспомогательная функция - фильтр. Проверяет вхождение элемента в массив.
        Если входит, вовращает индекс этого элемента.

        :param item: искомое значение
        :return: индекс или исключение

        '''

        if self.find(item) == -1:
            raise ValueError
        else:
            return self.find(item)

    def remove_of_index(self,index: int) -> None:

        '''

        Функция удаления элемента массива по индексу.

        :param index: int
        :return: None

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''
        if index <= self.__count-1 and index >= 0:
            for j in range(index, self.__count - 1, 1):
                self.__memory[j] = self.__memory[j + 1]
            del self.__memory[self.__count - 1]
            self.__count -= 1
            self.__size -= 1
        else:
            raise IndexError

    def remove(self,item: any) -> None:
        '''

        Функция удаления элемента массива по значению.

        :param item: значение элемента
        :return: None

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''
        index_item = self.__index(item)
        self.remove_of_index(index_item)

    def count_item(self,item: any) -> int:
        '''

        Функция подсчета количества заданного элемента в массиве.

        :param item: элемент
        :return: int

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''
        count = 0
        for elem in self.__memory:
            if elem == item:
                count += 1

        return count

    def insert_of_index(self,item: any, index: int) -> None:
        '''

        Функция вставки элемента на определенный индекс.

        :param item: значение элемента
        :param index: int
        :return: None

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''
        if self.__count == self.__size:
            new_memory = self.__memory_allocation()
            self.__memory = new_memory

        if index == 0: return self.add_front(item)
        if index >= self.__count: return self.add(item)

        if index < self.__count and index > 0:
            for i in range(self.__count - 1, index - 1, -1):
                self.__memory[i + 1] = self.__memory[i]

            self.__memory[index] = item
            self.__count += 1

    def is_empty(self) -> bool:
        '''

        Функция проверяет что память под массив пуста.

        :return: bool

        Временная сложность:
        Лучший: О(1)
        Средний: О(n)
        Худший: О(n)

        '''
        if self.count_item(None) == self.__size:
            return True
        return False
