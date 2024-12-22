from DZ_5.HogwartsSchedule import *

#Создал классы
clas = HogwartsClass('История', 'Олег', '9:15')
clas1 = HogwartsClass('Литература', 'Анна', '10:15')
clas2 = HogwartsClass('МатАн', 'Игорь', '13:15')

#Создал циклический список
circleL = HogwartsSchedule()
print('Cписок пуст?', circleL.IsEmpty(),'Количество элементов: ', circleL.count)
#Добавил классы в список
circleL.Add(clas)
circleL.Add(clas1)
circleL.Add(clas2)
print()
#Вывел список в виде массива
print('Исходный массив:',circleL.print_list())
print('Cписок пуст?', circleL.IsEmpty(),'Количество элементов: ', circleL.count)
#Вывел список через Next
print('\nСписок циклом 6 итераций')
for i in range(6):
    print(circleL.Next())


print()
print('Перешел к первому элементу: ', 'История')
circleL.Next()
print('Вывел на экран значение текущего элемента: ',circleL.GetCurrent())

print()
print('Удалил первый элемент')
circleL.RemoveCurrent()
print('Массив после удаления:',circleL.print_list())
print('Cписок пуст?', circleL.IsEmpty(),'Количество элементов: ', circleL.count)
#Вывел список через Next

print()
print('Вывел на экран значение текущего элемента: ',circleL.GetCurrent())

print('Перешел к последнему элементу: ', 'МатАн')
circleL.Next()
print('Вывел на экран значение текущего элемента: ',circleL.GetCurrent())

print('\nСписок циклом 6 итераций')
for i in range(6):
    print(circleL.Next())

print()
print('Удалил последний элемент')
circleL.RemoveCurrent()
print('Массив после удаления:',circleL.print_list())
print('Cписок пуст?', circleL.IsEmpty(),'Количество элементов: ', circleL.count)

print('\nСписок циклом 6 итераций')
for i in range(6):
    print(circleL.Next())

print()
print('Вывел на экран значение текущего элемента: ',circleL.GetCurrent())

print()
print('Удалил последний элемент')
circleL.RemoveCurrent()
print('Массив после удаления:',circleL.print_list())
print('Cписок пуст?', circleL.IsEmpty(),'Количество элементов: ', circleL.count)