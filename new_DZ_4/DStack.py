class DStack:


    def __init__(self, capacity = None):

        self.__capacity = capacity or 10
        self.__count = 0
        self.__memory = [None] * self.__capacity

    def __memory_alloc(self):

        self.__capacity = self.__capacity + 1 + self.__capacity // 2
        new_memory = [None] * self.__capacity
        for i, elem in enumerate(self.__memory):
            new_memory[i] = elem
        return new_memory

    def get(self):
        return self.__capacity, self.__memory, self.__count

    def push(self,item:any) -> None: #Добавляет элемент на вершину стека

        '''

         Добавить элемент в вершину стека. При переполнении массива
        увеличить размер (например, в 2 раза).

        :param item:элемент
        :return:None

        '''

        if self.__count == self.__capacity:
            self.__memory = self.__memory_alloc()

        self.__memory[self.__count] = item
        self.__count += 1

    def pop(self) -> any: #Удаляет и возвращает элемент с вершины стека. Если стек пуст, возвращает None.

       '''
       Извлечь последний добавленный элемент. Если стек пуст, выбросить
       исключение (например, IndexError или ValueError).

       :return: последний добавленный элемент

       '''

       if self.is_empty():
        return None

       buff = self.__memory[self.__count-1]
       del self.__memory[self.__count-1]
       self.__capacity -=1
       self.__count -= 1

       return buff

    def peek(self) -> any: #Возвращает элемент с вершины стека без его удаления. Если стек пуст, возвращает None.
        '''

         Вернуть верхний элемент без удаления, если стек пуст – выбросить исключение.
        :return: верхний элемент

        '''
        return self.__memory[self.__count-1]

    def is_empty(self) -> bool: #Возвращает true, если стек пуст, иначе false.
        return self.__count == 0

    def find(self,item:any) -> int:# вернуть позицию элемента в стеке, иначе вернуть -1
        '''

        Поиск элемента в стеке. Если элемент найден, вернуть его позицию
        (например, от начала массива, либо позицию относительно вершины), иначе
        вернуть -1.

        :param item: искомый элемент
        :return: индекс или -1

        '''
        index = -1

        for i in range(self.__count):
            if self.__memory[i] == item:
                index = i

        return index