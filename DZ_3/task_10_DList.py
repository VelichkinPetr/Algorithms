class DList:
    def __init__(self):
        self.size = 1
        self.count = 0
        self.array = [None]*self.size

    def __str__(self):
        array_out = []
        for elem in self.array:
            if elem != None:
                array_out.append(elem)
        return f'{array_out}'

    def __memory_allocation(self):
        self.size = self.size + 1 + self.size // 2
        new_memory = [None] * self.size
        for i, elem in enumerate(self.array):
            new_memory[i] = elem
        return new_memory

    def add(self,item):
        if self.count == self.size:
            new_array = self.__memory_allocation()
            self.array = new_array

        self.array[self.count] = item
        self.count += 1


    def add_front(self,item):
        if self.count == self.size:
            new_array = self.__memory_allocation()
            self.array = new_array

        for i in range(0, self.count, 1):
            buff = self.array[self.count - 1 - i]
            self.array[self.count - i] = buff
        self.array[0] = item
        self.count += 1

    def find(self,item):
        for i, elem in enumerate(self.array):
            if elem == item:
                return i
        return -1

    def __index(self,item):
        if self.find(item) == -1:
            raise ValueError
        else:
            return self.find(item)

    def remove_of_index(self,index):
        if index <= self.count-1 and index >= 0:
            for j in range(index, self.count-1, 1):
                self.array[j] = self.array[j + 1]
            del self.array[self.count-1]
            self.count -= 1
            self.size -= 1
        else:
            raise IndexError

    def remove(self,item):
        index_item = self.__index(item)
        self.remove_of_index(index_item)

    def count_item(self,item):
        count = 0
        for elem in self.array:
            if elem == item:
                count += 1
        return count

    def insert_of_index(self,item, index):
        if self.count == self.size:
            new_array = self.__memory_allocation()
            self.array = new_array
        if index <= self.count-1:
            for i in range(self.count-1,index-1, -1):
                self.array[i+1] = self.array[i]
            self.array[index] = item
            self.count += 1
        else: self.array[self.count] = item

    def is_empty(self):
        if self.count_item(None) == self.size:
            return True
        return False