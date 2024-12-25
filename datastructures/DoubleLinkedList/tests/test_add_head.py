import pytest
from datastructures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, [2, 1]),
                             (3, [3, 2, 1]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1, input_data + 1):
        dl.add_head(i)
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ([1], [[1]]),
                             ('', ['']),
                             ('0', ['0']),
                             (0, []),
                             (1, [1]),
                             (100, [i for i in range(100,0,-1)]),
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    if isinstance(input_data, int):
        for i in range(1, input_data + 1):
            dl.add_head(i)
    else:
        dl.add_head(input_data)
    assert dl.print_DoubleLinkedList() == expected