

class LinkedList:

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None

    def add_head(self,item:any)-> None:
        node = LinkedList.Node(data=item, next=None)

        if not self.size == 0:
            node.next = self.head

        self.head = node
        self.size+=1

    def add(self,item:any)-> None:
        node = LinkedList.Node(data=item, next=None)

        if self.size == 0:
            self.head = node
        else:
            iterator = self.head

            while iterator.next != None:
                iterator = iterator.next

            iterator.next = node

        self.size += 1

    def insert(self,item:any, position:int)-> None:
        node = LinkedList.Node(data=item, next=None)

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
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        raise ValueError

    def remove(self) -> any:
        if not self.is_empty():
            iterator = self.head
            counter = 1

            if self.size == 1:
                self.head = None
                self.size = 0
                return

            while counter != self.size-1:
                if self.size-1 != 0:
                    iterator = iterator.next
                    counter += 1

            data = iterator.next.data

            iterator.next = None
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
            if iterator.data == item:
                return True

            while iterator.next != None:
                if iterator.next.data == item:
                    return True

                iterator = iterator.next

        return False

    def clear(self) -> None:
        self.head = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def print_LinkedList(self) -> list:
        if not self.is_empty():
            iterator = self.head
            rez = [iterator.data]
            while iterator.next!= None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez

        return []