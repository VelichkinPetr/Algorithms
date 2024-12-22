from DZ_5.AvengersPriorityQueue import *

#Создал Очередь с приоритетом
pq = AvengersPriorityQueue()
#Создал данные для внесения в очередь
mission = AvengersMission('mission',1)
mission2 = AvengersMission('mission2',2)
mission3 = AvengersMission('mission3',2)
mission4 = AvengersMission('mission4',3)
#Записал данные в очередь
pq.enqueue(mission)
pq.enqueue(mission2)
pq.enqueue(mission3)
pq.enqueue(mission4)
#Удалил элемент с наибольшим приоритетом
print('элемент с наибольшим приоритетом: ',pq.dequeue(order_by=lambda x,y:x>y))
#Удалил элемент с наименьшим приоритетом
print('элемент с наименьшим приоритетом: ',pq.dequeue(order_by=lambda x,y:x<y))
#Удалил элемент с наименьшим приоритетом(приоритет двух оставшихся элементов равен, значит удаляем первый от головы)
print('приоритет двух оставшихся элементов равен, значит удаляем первый от головы:',pq.dequeue(order_by=lambda x,y:x>y))
print(pq.print_PriorityQueue())