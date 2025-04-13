from __future__ import annotations

class SortedLinkedList:

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, sort_list = None):

        if isinstance(sort_list, SortedLinkedList):
            self._size = sort_list._size
            self._head = sort_list._head
        else:
            self._size = 0
            self._head = None


    def add(self, item: any) -> None:

        '''

        Добавить элемент в список таким образом, чтобы поддерживать
        сортировку. При добавлении следует проходить по списку и найти первую
        позицию, где вставляемый элемент не нарушает отсортированность (при
        равных значениях можно вставлять новый элемент после уже существующих).

        :param item: элемент
        :return: None

        '''
        node = SortedLinkedList.Node(data=item, next=None)

        if self._size == 0:
            self._head = node
        else:
            iterator = self._head

            if iterator.data > node.data:
                self._head = node
                node.next = iterator
            else:
                while iterator.next is not None and iterator.next.data < node.data:
                    iterator = iterator.next

                buff = iterator.next
                iterator.next = node
                node.next = buff


        self._size += 1

    def remove(self, item:any) -> None:

        '''

         Удалить первое вхождение указанного элемента. Если элемент
        не найден, необходимо породить исключение ValueError.

        :return: None or ValueError

        '''
        if self.is_empty():
            raise ValueError

        if self._head.data == item:
            self._head = self._head.next
        else:
            iterator = self._head
            while iterator.next != None and iterator.next.data != item:
                iterator = iterator.next

            if not isinstance(iterator.next, SortedLinkedList.Node):
                raise ValueError

            iterator.next = iterator.next.next
        self._size -= 1

    def pop_front(self) -> any:
        '''

         Удалить и вернуть первый элемент списка (минимальное
        значение, так как список отсортирован). Если список пуст, породить
        исключение (например, ValueError).

        :return: первый элемент списка

        '''
        if self.is_empty():
            raise ValueError

        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data

    def pop_back(self) -> any:
        '''

        Удалить и вернуть последний элемент списка (максимальное
        значение). Если список пуст, породить исключение.

        :return: последний элемент списка

        '''

        if self.is_empty():
            raise ValueError

        if self._size == 1:
            data = self._head.data
            self._head = None
            self._size = 0
        else:

            iterator = self._head
            counter = 1
            while counter != self._size-1:
                iterator = iterator.next
                counter += 1

            data = iterator.next.data
            iterator.next = None
            self._size -= 1

        return data

    def merge(self,other_list:SortedLinkedList) -> SortedLinkedList:
        '''

         Объединить текущий список с другим отсортированным
        списком other_list и вернуть новый объект SortedLinkedList, содержащий все
        элементы из обоих списков в отсортированном порядке.

        :param other_list: отсортированный список
        :return: новый объект SortedLinkedList

        '''

        if not isinstance(other_list, SortedLinkedList):
            raise TypeError

        new_sorted_list = SortedLinkedList()

        iterator = self._head
        new_sorted_list.add(iterator.data)
        while iterator.next is not None:
            new_sorted_list.add(iterator.next.data)
            iterator = iterator.next

        iterator = other_list._head
        new_sorted_list.add(iterator.data)
        while iterator.next is not None:
            new_sorted_list.add(iterator.next.data)
            iterator = iterator.next

        return new_sorted_list

    def find(self, item: any) -> int:
        '''

        Поиск элемента в списке. Если элемент найден, вернуть
        его индекс (нумерация начинается с 0), в противном случае – вернуть -1.

        :param item: искомое значение
        :return: индекс или -1

        '''

        index = -1
        if self.is_empty():
            return index


        if self._head.data == item:
            index += 1
            return index
        else:
            index = 1
            iterator = self._head
            while iterator.next is not None and iterator.next.data != item:

                iterator = iterator.next
                index += 1
            if iterator.next is None and index == self._size:
                index = -1
        return index

    def is_empty(self) -> bool:
        '''

        Вернуть True, если список пуст, и False в противном случае.

        :return: bool

        '''
        return self._size == 0

    def count_item(self) -> int:
        '''
        :return:число элементов в списке
        '''
        return self._size

    def print_LinkedList(self) -> list:
        if not self.is_empty():
            iterator = self._head
            rez = [iterator.data]
            while iterator.next != None:
                iterator = iterator.next
                rez.append(iterator.data)
            return rez

        return []
