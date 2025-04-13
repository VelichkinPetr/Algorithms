
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
        if self.__count == self.__capacity:
            self.__memory = self.__memory_alloc()

        self.__memory[self.__count] = item
        self.__count += 1

    def pop(self) -> any: #Удаляет и возвращает элемент с вершины стека. Если стек пуст, возвращает None.
        if self.is_empty():
            return None

        buff = self.__memory[self.__count-1]
        del self.__memory[self.__count-1]
        self.__capacity -=1
        self.__count -= 1

        return buff

    def peek(self) -> any: #Возвращает элемент с вершины стека без его удаления. Если стек пуст, возвращает None.
        return self.__memory[self.__count-1]

    def is_empty(self) -> bool: #Возвращает true, если стек пуст, иначе false.
        return self.__count == 0

    def find(self,item:any) -> int:# вернуть позицию элемента в стеке, иначе вернуть -1
        index = -1

        for i in range(self.__count):
            if self.__memory[i] == item:
                index = i

        return index




