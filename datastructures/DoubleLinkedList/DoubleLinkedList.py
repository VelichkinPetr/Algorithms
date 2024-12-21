class Node:

    def __init__(self, data, next= None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add_head(self,item:any)-> None:
        node = Node(data=item, next=None)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size+=1

    def add(self,item:any)-> None:
        node = Node(data=item, next=None)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def insert(self,item:any, position:int)-> None:
        node = Node(data=item, next=None)

        if position == 1:
            return self.add_head(item)
        if position < 1 or position > self.size:
            raise IndexError

        iterator = self.head
        counter = 1

        while counter != position - 1:
            iterator = iterator.next
            counter += 1

        node.next = iterator.next
        iterator.next = node
        self.size += 1

    def remove_head(self) -> any:
        if self.is_empty():
            return None
        data = self.head.data
        if self.size > 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        self.size -= 1
        return data

    def remove(self) -> any:
        if self.is_empty():
            return None
        data = self.tail.data
        if self.size > 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def remove_position(self,position:int) -> any:
        if position == 1:
            return self.remove_head()
        if position < 1 or position > self.size:
            raise IndexError

        iterator = self.head
        counter = 1

        while counter != position - 1:
            iterator = iterator.next
            counter += 1

        data = iterator.next.data

        iterator_next = iterator.next.next
        iterator.next = iterator_next
        self.size += 1
        return data

    def search(self, item:any) -> bool:
        if not self.is_empty():
            iterator = self.head
            while iterator.next != None:
                if iterator.data == item:
                    return True
                elif iterator.next.data == item:
                    return True

                iterator = iterator.next
        return False

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def print_DoubleLinkedList(self) -> list:
        if not self.is_empty():
            iterator = self.head
            rez = [iterator.data]
            while iterator.next!= None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez
        else:
            return []