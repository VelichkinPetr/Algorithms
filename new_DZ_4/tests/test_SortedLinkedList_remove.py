import pytest
from new_DZ_4.SortedLinkedList import SortedLinkedList

@pytest.fixture(scope='function')
def sort_list():
    list_sort = SortedLinkedList()
    for i in range(5,0,-1):
        list_sort.add(i)
    return list_sort

@pytest.mark.parametrize('data, expected',
                         [
                             (5, [1,2,3,4]),
                             (4, [1,2,3,5]),
                             (3, [1,2,4,5]),
                             (2, [1,3,4,5])
                         ])

def test_positive(sort_list,data,expected):
    sort_list.remove(data)
    assert sort_list.print_LinkedList() == expected

@pytest.mark.parametrize('data, expected',
                         [
                             (5, [])
                         ])

def test_bound(sort_list,data,expected):
    for i in range(data, 0, -1):
        sort_list.remove(i)
    assert sort_list.print_LinkedList() == expected

@pytest.mark.parametrize('data, expected',
                         [
                             ([1], ValueError),
                             ('', ValueError),
                             ('0', ValueError)
                         ])

def test_negative(sort_list,data,expected):
    with pytest.raises(expected):
            sort_list.remove(data)
