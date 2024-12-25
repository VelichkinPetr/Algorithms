import pytest
from datastructures.LinkedList.LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [2,3,4]),
                             (2, [3,4]),
                             (3, [4])
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    for i in range(0,input_data):
        l.remove_head()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [])
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    for i in range(1,input_data+1): #[1,2,3,4]
        l.add(i)
    l.remove_head()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, ValueError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        l = LinkedList()
        l.remove_head()