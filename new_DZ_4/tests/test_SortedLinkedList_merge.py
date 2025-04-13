import pytest
from new_DZ_4.SortedLinkedList import SortedLinkedList

@pytest.fixture(scope='function')
def sort_list():
    list_sort = SortedLinkedList()
    list_sort_2 = SortedLinkedList()

    return list_sort, list_sort_2

@pytest.mark.parametrize('list1, list2, expected',
                         [
                             ( [1,2,3,4,5],[6,7,8],[1,2,3,4,5,6,7,8]),
                             ( [1,2,3,4,5],[1],[1,1,2,3,4,5]),
                             ( [88,9,56],[1],[1,9,56,88])
                         ])

def test_positive(sort_list,list1, list2,expected):
    sort_list1, sort_list2 = sort_list

    for elem in list1:
        sort_list1.add(elem)
    for elem in list2:
        sort_list2.add(elem)

    sort_list3 = sort_list1.merge(sort_list2)
    assert  sort_list3.print_LinkedList() == expected

@pytest.mark.parametrize('list1, list2, expected',
                         [
                             ([2],[4],[2,4])
                         ])

def test_bound(sort_list,list1, list2,expected):
    sort_list1, sort_list2 = sort_list

    for elem in list1:
        sort_list1.add(elem)
    for elem in list2:
        sort_list2.add(elem)

    sort_list3 = sort_list1.merge(sort_list2)
    assert sort_list3.print_LinkedList() == expected

@pytest.mark.parametrize('list1, list2, expected',
                         [
                             ([],'0', AttributeError),
                             ([],0, AttributeError),
                             (0,0, AttributeError)
                         ])

def test_negative(sort_list,list1, list2,expected):
    with pytest.raises(expected):
        sort_list1, sort_list2 = sort_list
        sort_list1.merge(sort_list2)
