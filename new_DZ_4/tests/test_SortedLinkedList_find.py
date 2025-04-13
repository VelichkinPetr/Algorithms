import pytest
from new_DZ_4.SortedLinkedList import SortedLinkedList

@pytest.fixture(scope='session')
def sort_list():
    list_sort = SortedLinkedList()
    for i in range(5,0,-1):
        list_sort.add(i)
    return list_sort

@pytest.mark.parametrize('data, expected',
                         [
                             ( 1, 0 ),
                             ( 2, 1 ),
                             ( 3, 2 ),
                             ( 4, 3 ),
                             ( 5, 4 )
                         ])

def test_positive(sort_list,data,expected):
    assert sort_list.find(data) == expected

@pytest.mark.parametrize('data, expected',
                         [
                             ( 0, -1 ),
                             ( 6, -1 ),
                         ])

def test_bound(sort_list,data,expected):
    assert sort_list.find(data) == expected

