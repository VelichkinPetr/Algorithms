class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self,item:any) -> None: #Добавляет элемент в конец очереди.
        node = Node(data=item, next=None)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self) -> any: #Удаляет и возвращает первый элемент из очереди. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self) -> any or None: #Возвращает первый элемент из очереди без его удаления. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self) -> bool: #Возвращает true, если очередь пуста, иначе false.
        return self.size == 0

    def count(self) -> int: #Возвращает количество элементов в очереди.
        return self.size

    def print_Queue(self) -> list:
        if not self.is_empty():
            iterator = self.head
            rez = [iterator.data]
            while iterator.next != None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez
        else:
            return []
