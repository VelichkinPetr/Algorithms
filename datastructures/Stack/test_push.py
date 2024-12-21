import pytest
from Stack import Stack

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [2,1]),
                             (3, [3, 2, 1]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1])
                         ])

def test_positive(input_data,expected):
    s = Stack()
    for i in range(1,input_data+1):
        s.push(i)
    assert s.print_Stack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             ('', ['']),
                             ([], [[]])
                         ])

def test_bound(input_data,expected):
    s = Stack()
    s.push(input_data)
    assert s.print_Stack() == expected