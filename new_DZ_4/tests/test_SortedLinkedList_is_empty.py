import pytest
from new_DZ_4.SortedLinkedList import SortedLinkedList

@pytest.fixture(scope='session')
def sort_list():
    return SortedLinkedList()

@pytest.mark.parametrize('data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_positive(sort_list,data,expected):
    for i in range(0, data):
        sort_list.add(i)
    assert sort_list.is_empty() == expected

