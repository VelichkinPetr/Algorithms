class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DeQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def pushFront(self,item:any) -> any: #Добавляет элемент в начало очереди.
        node = Node(data=item, next=None, prev=None)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1

    def pushBack(self,item:any) -> any: #Добавляет элемент в конец очереди.
        node = Node(data=item, next=None, prev=None)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def popFront(self) -> any: #Удаляет и возвращает первый элемент из очереди. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        data = self.head.data
        if self.count() > 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        self.size -= 1
        return data

    def popBack(self) -> any: #Удаляет и возвращает последний элемент из очереди. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        data = self.tail.data
        if self.count() > 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def peekFront(self) -> any or None: #Возвращает первый элемент из очереди без его удаления. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        return self.head.data

    def peekBack(self) -> any or None: #Возвращает первый элемент из очереди без его удаления. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        return self.tail.data

    def is_empty(self) -> bool: #Возвращает true, если очередь пуста, иначе false.
        return self.size == 0

    def count(self) -> int: #Возвращает количество элементов в очереди.
        return self.size

    def print_DeQueue(self) -> list:
        if not self.is_empty():
            iterator = self.head
            rez = [iterator.data]
            while iterator.next != None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez
        else:
            return []