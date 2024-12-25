import pytest
from datastructures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [2,3,4]),
                             (2, [1,3,4]),
                             (3, [1,2,4]),
                             (4, [1,2,3])
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5): #[1,2,3,4]
        dl.add(i)
    dl.remove_position(input_data)
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [])
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    dl.remove_position(input_data)
    assert dl.print_DoubleLinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (5, IndexError),
                             (0, IndexError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        dl = DoubleLinkedList()
        for i in range(1, 5):  # [1,2,3,4]
            dl.add(i)
        dl.remove_position(input_data)