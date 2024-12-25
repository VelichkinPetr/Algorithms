import pytest
from datastructures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1,2,3]),
                             (2, [1,2]),
                             (3, [1]),
                             (4, []),
                             (5, [])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5): #[1,2,3,4]
        dl.add(i)
    for i in range(0,input_data):
        dl.remove()
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (4, []),
                             (5, [])
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5): #[1,2,3,4]
        dl.add(i)
    for i in range(0,input_data):
        dl.remove()
    assert dl.print_DoubleLinkedList() == expected