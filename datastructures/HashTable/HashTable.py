class LinkedList:
    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.__head = None
        self.__size = 0

    def add(self, item:any) -> None:
        node = LinkedList.Node(data=item, next=None)

        if self.__size == 0:
            self.__head = node
        else:
            iterator = self.__head

            while iterator.next != None:
                iterator = iterator.next

            iterator.next = node

        self.__size += 1

    def __getitem__(self, position:int) -> any:
        if position < 0 or position > self.__size - 1:
            raise IndexError

        iterator = self.__head
        counter = 0

        while counter != position:
            iterator = iterator.next
            counter += 1

        return iterator.data

    def search_by_key(self, key:any) -> any:
        if self.__size == 0: raise ValueError

        if self.__head.data[0] != key and self.__size == 1: return None

        iterator = self.__head
        if iterator.data[0] == key:
            return iterator.data[1]
        while iterator.next != None:
            if iterator.next.data[0] == key:
                return iterator.next.data[1]
            iterator = iterator.next
        return None

    def print_LinkedList(self) -> list:
        if not self.__size == 0:
            iterator = self.__head
            rez = [iterator.data]
            while iterator.next != None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez
        else:
            return []

class HashMap:

    def __init__(self):
        self.__count = 0
        self.__size = 100
        self.__memory = [None] * self.__size

    def add(self, key:any, item:any) -> None:
        hash = self.__hash_function(key)

        if self.__memory[hash] != None:
            if self.__memory[hash][0] != key:

                if not isinstance(self.__memory[hash], LinkedList):
                    ll = LinkedList()
                    ll.add(self.__memory[hash])
                    self.__memory[hash] = ll

                self.__memory[hash].add((key, item))

        else:
            self.__memory[hash] = (key, item)
        self.__count += 1

    def get(self, key:any) -> any:
        hash = self.__hash_function(key)

        if self.__memory[hash] == None:
            raise ValueError("Not exist!")

        if not isinstance(self.__memory[hash], LinkedList):
            return self.__memory[hash][1]
        else:
            item = self.__memory[hash].search_by_key(key)

        if item is None:
            raise ValueError("Not exist!")

        return item

    def clear(self) -> None:
        self.__count = 0
        self.__memory = [None] * self.__size

    def __hash_function(self, key:any) -> int:
        index = hash(key) % self.__size
        return index

    def __get_count(self) -> int:
        return self.__count

    count = property(__get_count)