from new_DZ_5.task_2_TaskStack import *

#Создал задачи
task1 = ProjectTask('1',(2020,10,17))
task2 = ProjectTask('2',(2020,10,18))
task3 = ProjectTask('3',(2020,10,19))

#Создал список
stack = TaskStack()
print(f'Стэк пуст?      {stack.is_empty()}')
print(f'Задач в списке: {stack.count()}\n')
#Добавил в вершину
stack.push(task1)
stack.push(task2)
stack.push(task3)
stack.__str__()

print(f'\nВершина Стэка: {stack.peek()}')

print(f'Удалили вершину Стэка: {stack.pop()}')
stack.__str__()
print(f'\nВершина Стэка: {stack.peek()}')