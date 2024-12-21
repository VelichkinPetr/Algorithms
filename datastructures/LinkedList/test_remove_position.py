import pytest
from LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [2,3,4]),
                             (2, [1,3,4]),
                             (3, [1,2,4]),
                             (4, [1,2,3])
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    l.remove_position(input_data)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [])
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    l.remove_position(input_data)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (5, IndexError),
                             (0, IndexError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        l = LinkedList()
        for i in range(1, 5):  # [1,2,3,4]
            l.add(i)
        l.remove_position(input_data)