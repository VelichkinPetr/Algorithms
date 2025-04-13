import pytest
from new_DZ_4.SortedLinkedList import SortedLinkedList

@pytest.fixture(scope='session')
def sort_list():
    list_sort = SortedLinkedList()
    for i in range(5,0,-1):
        list_sort.add(i)
    return list_sort

@pytest.mark.parametrize('expected',
                         [
                             ( [2,3,4,5]),
                             ( [3,4,5]),
                             ( [4,5]),
                             ( [5])
                         ])

def test_positive(sort_list,expected):
    sort_list.pop_front()
    assert sort_list.print_LinkedList() == expected

@pytest.mark.parametrize('expected',
                         [
                             ([])
                         ])

def test_bound(sort_list,expected):

    sort_list.pop_front()
    assert sort_list.print_LinkedList() == expected

@pytest.mark.parametrize('data, expected',
                         [
                             ([1], ValueError),
                             ('', ValueError),
                             ('0', ValueError)
                         ])

def test_negative(sort_list,data,expected):
    with pytest.raises(expected):
            sort_list.pop_front()
