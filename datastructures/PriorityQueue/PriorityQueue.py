class Task:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        self._check_int()

    def _check_int(self):
        if not isinstance(self.priority, int):
            raise TypeError

class PriorityQueue:

    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self,item:any) -> None: #Добавляет элемент в конец очереди.
        if not isinstance(item,Task):
            raise AttributeError

        node = PriorityQueue.Node(data=item, next=None,prev = None)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.size += 1

    def dequeue(self, order_by=lambda x,y: x>y) -> any: #Удаляет и возвращает элемент из очереди по приоритету. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None

        if self.size == 1:
            data = self.head.data.task
            self.head = None
        else:
            target_node = self.head
            target_priority = self.head.data.priority
            iterator = self.head

            while iterator.next != None:

                if order_by(iterator.next.data.priority ,target_priority):
                    target_priority = iterator.next.data.priority
                    target_node = iterator.next

                iterator = iterator.next

            data = target_node.data.task

            if target_node == self.head:
                self.head = self.head.next
            elif target_node == self.tail:
                self.tail = target_node.prev
                target_node.prev.next = target_node.next
            else:
                target_node.next.prev = target_node.prev
                target_node.prev.next = target_node.next
        self.size -= 1

        return data

    def peek(self,order_by=lambda x,y: x>y) -> any or None: #Возвращает элемент из очереди, по приоритету(мин, макс) без его удаления. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None

        if self.size == 1:
            return self.head.data.task

        else:
            target_node = self.head
            target_priority = self.head.data.priority
            iterator = self.head

            while iterator.next != None:
                if order_by(iterator.next.data.priority ,target_priority):
                    target_priority = iterator.next.data.priority
                    target_node = iterator.next
                iterator = iterator.next

            return target_node.data.task

    def is_empty(self) -> bool: #Возвращает true, если очередь пуста, иначе false.
        return self.size == 0

    def count(self) -> int: #Возвращает количество элементов в очереди.
        return self.size

    def print_PriorityQueue(self) -> list:
        if not self.is_empty():
            iterator = self.head
            rez = [iterator.data.task]
            while iterator.next != None:
                iterator = iterator.next
                rez.append(iterator.data.task)
            return rez

        return []
