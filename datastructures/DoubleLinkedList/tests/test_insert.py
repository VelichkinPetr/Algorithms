import pytest
from datastructures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,1), [7,1,2,3,4]),
                             ((7,2), [1,7,2,3,4]),
                             ((7,3), [1,2,7,3,4]),
                             ((7,4), [1,2,3,7,4])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5):#[1,2,3,4]
        dl.add(i)
    dl.insert(*input_data)
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,1), [7]),
                             (('7',1), ['7']),
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    dl.insert(*input_data)
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,0), IndexError),
                             ((7,5), IndexError),
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        dl = DoubleLinkedList()
        for i in range(1,5):#[1,2,3,4]
            dl.add(i)
        dl.insert(*input_data)