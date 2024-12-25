import pytest
from datastructures.Stack.Stack import Stack

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 2),
                             (2, 4),
                             (3, 6),
                             (4, 8),
                             (5, 10)
                         ])

def test_positive(input_data,expected):
    s = Stack()
    for i in range(1,input_data+1):
        (s.push(i*2))
    assert s.peek() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_bound(input_data,expected):
    s = Stack()
    s.push(input_data)
    s.pop()
    assert s.peek() == expected
