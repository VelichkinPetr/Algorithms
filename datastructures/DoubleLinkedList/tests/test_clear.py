import pytest
from datastructures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, []),
                             (3, []),
                             (4, [])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(0,input_data):
       dl.add(i)
    dl.clear()
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, []),
                             (1, []),
                             (100,[])
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(0,input_data):
        dl.add(i)
    dl.clear()
    assert dl.print_DoubleLinkedList() == expected