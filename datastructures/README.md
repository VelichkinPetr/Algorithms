# Структуры данных(DataStructures)

## Определение

Структура данных (англ. data structure) — способ организации данных и правил(интерфейса) работы с ними. 
Следует различать понятия логической и физической структур.\
Логическая структура - это абстрактная схема расположения данных.\
Физическая структура – это способ (или схема) конкретного размещения данных в памяти компьютера.\
Интерфейс - набор функций для добавления, поиска, изменения и удаления данных.

## Линейные структуры данных

+ `LinkеdList` - структура данных, состоящая из узлов, каждый из которых хранит значение и 
ссылку на следующий узел в списке.
  + `DoubleLinkedList` - структура данных, состоящая из узлов, каждый из которых хранит значение и 
ссылки на следующий и предыдущий узлы.
+ `Stack` - это абстрактный тип данных (АТД), следует принципу 
"последний пришел — первый ушел" (LIFO, Last In First Out)
+ `Queue` - это абстрактный тип данных (АТД), "первый пришел — первый ушел" (FIFO, First In First
 Out)
  + `PriorityQueue` - это абстрактный тип данных (АТД), наподобие стека или очереди, 
где у каждого элемента есть приоритет
+ `DeQueue` - эта структура поддерживает как FIFO, так и LIFO
+ `HashTable(HashMap)` - структура данных, состоящая из пар «ключ-значение»,
где у ключей есть хэши, то есть числовые уникальные идентификаторы.

