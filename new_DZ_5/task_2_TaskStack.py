from datetime import date
class ProjectTask:
    def __init__(self,Description:str, DueDate: date):
        self.Description = Description
        self.DueDate = DueDate

    def __str__(self):
        return f'{self.Description}, {date(*self.DueDate)}'

class Node:
    def __init__(self,data,prev = None):
        self.data = data
        self.prev = prev

class TaskStack:
    def __init__(self):
        self.size = 0
        self.top = None


    def push(self,task:ProjectTask): #Добавляет новую задачу task на вершину стека
        node = Node(task, prev=None)
        node.prev = self.top
        self.top = node
        self.size += 1


    def pop(self): #Удаляет и возвращает задачу с вершины стека. Если стек пуст, возвращает None.
        if self.is_empty():
            return None
        buff = self.top.data
        self.top = self.top.prev
        self.size -= 1
        return buff

    def peek(self): #Возвращает задачу с вершины стека без её удаления. Если стек пуст, возвращает None.
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self): #Возвращает true, если стек пуст, иначе false.
        if self.size == 0:
            return True
        return False

    def count(self): #Возвращает количество задач в стеке.
        return self.size

    def __str__(self) -> None:
        if not self.is_empty():
            iterator = self.top
            print(iterator.data)
            while iterator.prev != None:
                iterator = iterator.prev
                print(iterator.data)
        else:
            print('Список пуст')