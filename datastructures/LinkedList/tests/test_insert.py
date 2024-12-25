import pytest
from datastructures.LinkedList.LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,1), [7,1,2,3,4]),
                             ((7,2), [1,7,2,3,4]),
                             ((7,3), [1,2,7,3,4]),
                             ((7,4), [1,2,3,7,4])
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(1,5):#[1,2,3,4]
        l.add(i)
    l.insert(*input_data)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,1), [7]),
                             (('7',1), ['7']),
                         ])

def test_bound(input_data,expected):
    l = LinkedList()
    l.insert(*input_data)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,0), IndexError),
                             ((7,5), IndexError),
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        l = LinkedList()
        for i in range(1,5):#[1,2,3,4]
            l.add(i)
        l.insert(*input_data)