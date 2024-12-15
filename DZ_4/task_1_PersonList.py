class PersonCard:

    def __init__(self, name:str, age:int, occupation:str):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return f'{self.name}, {self.age}, {self.occupation}'
class Node:

    def __init__(self, data, next= None):
        self.data = data
        self.next = next

class PersonList:

    def __init__(self):
        self.count = 0
        self.head = None

    def add_person(self,person:PersonCard)-> None:              #Добавляет новую карточку персоны person в начало списка.
        if not isinstance(person,PersonCard):
            raise TypeError
        node = Node(data=person, next=None)

        if self.count == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count+=1

    def append_person(self,person:PersonCard)-> None:                  #Добавляет новую карточку персоны person в конец списка.
        node = Node(data=person, next=None)

        if self.count == 0:
            self.head = node
        else:
            iterator = self.head

            while iterator.next != None:
                iterator = iterator.next

            iterator.next = node

        self.count += 1
    def insert_person_at(self,index:int, person:PersonCard)-> None or Exception:   #Вставляет новую карточку персоны person на позицию с указанным индексом. Если индекс выходит за границы списка, генерируется исключение.
        node = Node(data=person, next=None)

        if index < 1 or index > self.count:
            raise IndexError
        elif index == 1:
            return self.add_person(person)


        iterator = self.head
        counter = 1

        while counter != index - 1:
            iterator = iterator.next
            counter += 1

        node.next = iterator.next
        iterator.next = node
        self.count += 1

    def remove_first_person(self) -> PersonCard:                              #Удаляет первую карточку в списке и возвращает её.
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data

    def remove_last_person(self) -> PersonCard:                               #Удаляет последнюю карточку в списке и возвращает её.
        iterator = self.head
        counter = 1

        while counter != self.count - 1:
            iterator = iterator.next
            counter += 1

        data = iterator.next.data

        iterator.next = None
        self.count -= 1
        return data

    def remove_person(self,person:PersonCard) -> None:                  #Удаляет карточку персоны, соответствующую переданной person.
        iterator = self.head
        if iterator.data == person:
            return self.remove_first_person()

        while iterator.next != None:
            #print(iterator.next.data)
            if iterator.next.data == person:
                iterator.next = iterator.next.next
                self.count -= 1
                return
            iterator = iterator.next
        raise ValueError(f'({person}) нет в списке')

    def clear_all(self) -> None:                                        #Очищает список, удаляя все карточки.
        self.head = None
        self.count = 0

    def total_people(self) -> int:                                     #Возвращает количество карточек в списке.
        return self.count

    def is_empty(self) -> bool:                                         #Возвращает true, если список пуст, иначе false.
        if self.count == 0:
            return True
        return False

    def __str__(self) -> None:
        if not self.is_empty():
            iterator = self.head
            print(iterator.data)
            while iterator.next!= None:
                iterator = iterator.next
                print(iterator.data)
        else:
            print('Список пуст')

