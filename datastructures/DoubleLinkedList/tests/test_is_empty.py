import pytest
from datastructures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(0,input_data):
        dl.add(i)
    assert dl.is_empty() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False)
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(0,input_data):
        dl.add(i)
    assert dl.is_empty() == expected