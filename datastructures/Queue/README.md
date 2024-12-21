# Очередь (Queue)
## Определение

Очередь — это абстрактный тип данных (АТД), представляющий 
собой коллекцию элементов с двумя основными операциями: 
добавление элемента в конец очереди (enqueue) и удаление 
элемента из начала очереди (dequeue). Очередь следует 
принципу "первый пришел — первый ушел" (FIFO, First In First
 Out), что означает, что первый добавленный элемент будет 
первым удаленным.

## Операции
+ enqueue(item) - добавляет элемент в конец очереди
+ dequeue() - удаляет и возвращает первый элемент из очереди
+ peek() - возвращает первый элемент из очереди без его удаления.
+ count() - определяет количество элементов в очереди
+ is_empty() - проверяет, пуста ли очередь
+ print_Stack() - представляет очередь в виде массива

## Оценка временной сложности
| функция  | лучший  | средний  | худший |
|----------|---------|----------|--------|
| enqueue  | О(1)    | О(1)     | О(1)   |
| dequeue  | О(1)    | О(1)     | О(1)   |
| peek     | О(1)    | О(1)     | О(1)   |
| count    | О(1)    | О(1)     | О(1)   |
| is_empty | О(1)    | О(1)     | О(1)   |