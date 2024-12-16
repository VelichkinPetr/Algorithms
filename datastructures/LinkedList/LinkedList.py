class Node:

    def __init__(self, data, next= None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def add_head(self,item)-> None:
        node = Node(data=item, next=None)

        if self.size == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size+=1

    def add(self,item)-> None:
        node = Node(data=item, next=None)

        if self.size == 0:
            self.head = node
        else:
            iterator = self.head

            while iterator.next != None:
                iterator = iterator.next

            iterator.next = node

        self.size += 1

    def insert(self,item, position:int):
        node = Node(data=item, next=None)

        if position < 1 or position > self.size:
            raise IndexError
        elif position == 1:
            return self.add_head(item)


        iterator = self.head
        counter = 1

        while counter != position - 1:
            iterator = iterator.next
            counter += 1

        node.next = iterator.next
        iterator.next = node
        self.size += 1

    def remove_head(self) :
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        return ValueError

    def remove(self):
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

    def remove_position(self,position) -> None:
        if position < 1 or position > self.size:
            raise IndexError
        elif position == 1:
            return self.remove_head()


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

    def clear(self) -> None:
        self.head = None
        self.size = 0

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def print_LinkedList(self) -> None:
        if not self.is_empty():
            iterator = self.head
            rez = [iterator.data]
            while iterator.next!= None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez
        else:
            return []

l = LinkedList()
l.add(1)
l.add(2)
l.remove()

print(l.size)
r = l.print_LinkedList()
print(r)