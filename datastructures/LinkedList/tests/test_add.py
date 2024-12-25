import pytest
from datastructures.LinkedList.LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, [1,2]),
                             (3, [1,2,3]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5])
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(1,input_data+1):
        l.add(i)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ([1], [[1]]),
                             ('', ['']),
                             ('0', ['0']),
                             (0, []),
                             (1, [1]),
                             (100, [i for i in range(1,101)]),
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    if isinstance(input_data, int):
        for i in range(1, input_data + 1):
            l.add(i)
    else:
        l.add(input_data)
    assert l.print_LinkedList() == expected