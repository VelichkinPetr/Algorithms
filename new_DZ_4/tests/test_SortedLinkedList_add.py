import pytest
from new_DZ_4.SortedLinkedList import SortedLinkedList

@pytest.fixture(scope='session')
def sort_list():
    return SortedLinkedList()

@pytest.mark.parametrize('data, expected',
                         [
                             (5, [5]),
                             (4, [4,5]),
                             (3, [3,4,5]),
                             (2, [2,3,4,5])
                         ])

def test_positive(sort_list,data,expected):
    sort_list.add(data)
    assert sort_list.print_LinkedList() == expected

@pytest.mark.parametrize('data, expected',
                         [
                             ([1], TypeError),
                             ('', TypeError),
                             ('0', TypeError)
                         ])

def test_negative(sort_list,data,expected):
    with pytest.raises(expected):
            sort_list.add(data)
