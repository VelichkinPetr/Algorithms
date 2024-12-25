import pytest
from datastructures.LinkedList.LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, []),
                             (3, []),
                             (4, [])
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(0,input_data):
        l.add(i)
    l.clear()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, []),
                             (1, []),
                             (100,[])
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    for i in range(0,input_data):
        l.add(i)
    l.clear()
    assert l.print_LinkedList() == expected