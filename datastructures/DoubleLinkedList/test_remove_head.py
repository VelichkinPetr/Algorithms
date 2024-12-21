import pytest
from DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [2,3,4]),
                             (2, [3,4]),
                             (3, [4])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5): #[1,2,3,4]
        dl.add(i)
    for i in range(0,input_data):
        dl.remove_head()
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, []),
                             (0, [])
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,input_data+1): #[1,2,3,4]
        dl.add(i)
    dl.remove_head()
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, None)
                         ])

def test_negative(input_data,expected):
    dl = DoubleLinkedList()
    assert dl.remove_head() == expected