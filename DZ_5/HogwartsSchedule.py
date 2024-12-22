import datetime
class HogwartsClass:

    def __init__(self, desc:str ,instructor:str,starttime:datetime ):
        self.desc = desc
        self.instructor = instructor
        self.starttime = starttime
    def __str__(self):
        return f'{self.desc}, {self.instructor}, {self.starttime}'
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class HogwartsSchedule:
    def __init__(self):
        self.count = 0
        self.indicator = 0
        self.head = None
        self.tail = None

    def Add(self,clas:HogwartsClass): #Добавляет новый учебный класс в список.
        node = Node(data=clas, next=None)

        if self.count == 0:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        self.count += 1

    def Next(self):#Переходит к следующему классу в списке, возвращая его. Если достигнут конец списка, автоматически возвращается к первому элементу.
        if self.count == 0:
            return ValueError
        if self.indicator == 0:
            self.indicator = self.head
            return self.indicator.data
        self.indicator = self.indicator.next
        return self.indicator.data

    def RemoveCurrent(self): #Удаляет текущий класс из списка.
        if self.count == 0 or self.indicator == 0:
            raise ValueError
        if self.indicator == self.head:
            self.head = self.head.next
            self.tail.next = self.head
            self.indicator = self.head
        else:
            iterator = self.head
            while iterator.next != self.indicator and iterator.next != self.head:
                iterator = iterator.next
            self.indicator = iterator.next.next
            iterator.next = iterator.next.next
        self.count -= 1

    def GetCurrent(self): #Возвращает текущий класс без его изменения.
        if self.count == 0 or self.indicator == 0:
            raise ValueError
        return self.indicator.data

    def IsEmpty(self): #Возвращает true, если список пуст, иначе false.
        return self.count == 0

    def Count(self): #Возвращает количество классов в списке.
        return self.count

    def print_list(self) -> None:
        if not self.IsEmpty():
            iterator = self.head
            counter = 1
            rez = []
            rez.append(iterator.data.desc)
            while counter != self.count:
                iterator = iterator.next
                counter += 1
                rez.append(iterator.data.desc)
            return rez
        else:
            print('Список пуст')