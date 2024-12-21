import pytest
from LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1,2,3]),
                             (2, [1,2]),
                             (3, [1]),
                             (4, []),
                             (5, [])
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    for i in range(0,input_data):
        l.remove()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (4, []),
                             (5, [])
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    for i in range(0,input_data):
        l.remove()
    assert l.print_LinkedList() == expected