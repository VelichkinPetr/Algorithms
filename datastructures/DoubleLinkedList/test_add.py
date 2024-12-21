import pytest
from DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, [1,2]),
                             (3, [1,2,3]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,input_data+1):
        dl.add(i)
    assert dl.print_DoubleLinkedList() == expected

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
    dl = DoubleLinkedList()
    if isinstance(input_data, int):
        for i in range(1, input_data + 1):
            dl.add(i)
    else:
        dl.add(input_data)
    assert dl.print_DoubleLinkedList() == expected