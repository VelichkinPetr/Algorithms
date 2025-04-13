from new_DZ_5.task_3_PrintQueue import *

#Создал задачи
doc1 = PrintDocument('1',111)
doc2 = PrintDocument('2',222)
doc3 = PrintDocument('3',333)

#Создал очередь
queue = PrintQueue()
print(f'Очередь пуста?         {queue.is_empty()}')
print(f'Документов в очереди:  {queue.count_doc()}\n')

#Добавил в вершину
queue.enqueue(doc1)
queue.enqueue(doc2)
queue.enqueue(doc3)
queue.__str__()
print(f'Очередь пуста?         {queue.is_empty()}')
print(f'Документов в очереди:  {queue.count_doc()}\n')

print(f'\nПервый в очереди: {queue.peek()}')

print(f'Первый покинул очередь: {queue.dequeue()}')
queue.__str__()
print(f'\nПервый в очереди: {queue.peek()}')