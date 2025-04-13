from new_DZ_5.task_1_PersonList import *

#Создал карточки
Ivan = PersonCard('Ivan', 25, 'teacher')
Oleg = PersonCard('Олег', 22, 'инженер')
John = PersonCard('John', 35, 'trener')
Peter = PersonCard('Петр', 28, 'технолог')

#Создал список
pList = PersonList()

#Добавил в конец
pList.append_person(Oleg)
pList.append_person(Ivan)
pList.append_person(Peter)

#Добавил в начало
pList.add_person(Ivan)

#Добавил на 2 позицию
pList.insert_person_at(2,John)

pList.__str__()

#Удалил первого
first = pList.remove_first_person()
print(f'\nУдалил первый: {first}')
pList.__str__()

#Удалил последнего
last = pList.remove_last_person()
print(f'\nУдалил последний: {last}')
pList.__str__()

#Удалил второго
last = pList.remove_person(Oleg)
print(f'\nУдалил последний: {Oleg}')
pList.__str__()