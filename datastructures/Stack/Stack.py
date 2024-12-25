class Stack:

    class Node:
        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.size = 0
        self.top = None

    def push(self,item:any) -> None: #Добавляет элемент на вершину стека
        node = Stack.Node(item, prev=None)
        node.prev = self.top
        self.top = node
        self.size += 1

    def pop(self) -> any: #Удаляет и возвращает элемент с вершины стека. Если стек пуст, возвращает None.
        if self.is_empty():
            return None

        buff = self.top.data
        self.top = self.top.prev
        self.size -= 1

        return buff

    def peek(self) -> any: #Возвращает элемент с вершины стека без его удаления. Если стек пуст, возвращает None.
        if self.is_empty():
            return None

        return self.top.data

    def is_empty(self) -> bool: #Возвращает true, если стек пуст, иначе false.
        return self.size == 0

    def count(self) -> int: #Возвращает количество элементов в стеке.
        return self.size

    def print_Stack(self) -> list:
        if not self.is_empty():
            iterator = self.top
            rez = [iterator.data]
            while iterator.prev != None:
                iterator = iterator.prev
                rez.append(iterator.data)
            return rez

        return []