import pytest
from DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, True),
                             (3, True),
                         ])

def test_positive(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5):
        dl.add(i)
    assert dl.search(input_data) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, False),
                             (1, True),
                             (4, True),
                             (5, False),
                             ('', False),
                             ([], False)
                         ])

def test_bound(input_data,expected):
    dl = DoubleLinkedList()
    for i in range(1,5):
        dl.add(i)
    assert dl.search(input_data) == expected