import pytest
from HashTable import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 3),
                             (3, 4),
                             (4, 5),
                             (5, 6)
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(1,6):
        l.add((i,i+1))
    assert l.search_by_key(input_data) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, None),
                             (1, 2),
                             (5, 6),
                             (6,None)
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    for i in range(1,6):
        l.add((i,i+1))
    assert l.search_by_key(input_data) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, ValueError),
                             (1, ValueError),
                             (5, ValueError),
                             (6,ValueError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        l = LinkedList()
        l.search_by_key(input_data) == expected