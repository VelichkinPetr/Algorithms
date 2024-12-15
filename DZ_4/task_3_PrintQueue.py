class PrintDocument:
    def __init__(self,Title :str, NumberOfPages : int):
        self.Title = Title
        self.NumberOfPages = NumberOfPages
    def __str__(self):
        return f'{self.Title}, {self.NumberOfPages}'
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class PrintQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self,document:PrintDocument): #Добавляет документ document в конец очереди.
        node = Node(document, next=None)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self): #Удаляет и возвращает первый документ из очереди. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self): #Возвращает первый документ из очереди без его удаления. Если очередь пуста, возвращает None.
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self): #Возвращает true, если очередь пуста, иначе false.
        if self.size == 0:
            return True
        return False

    def count_doc(self): #Возвращает количество документов в очереди.
        return self.size

    def __str__(self) -> None:
        if not self.is_empty():
            iterator = self.head
            print(iterator.data)
            while iterator.next != None:
                iterator = iterator.next
                print(iterator.data)
        else:
            print('Список пуст')

doc1 = PrintDocument('1',111)
doc2 = PrintDocument('2',222)
doc3 = PrintDocument('3',333)

queue = PrintQueue()
queue.enqueue(doc1)
queue.enqueue(doc2)
queue.enqueue(doc3)
queue.__str__()