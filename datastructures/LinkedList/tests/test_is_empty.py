import pytest
from datastructures.LinkedList.LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_positive(input_data,expected):
    l = LinkedList()
    for i in range(0,input_data):
        l.add(i)
    assert l.is_empty() == expected