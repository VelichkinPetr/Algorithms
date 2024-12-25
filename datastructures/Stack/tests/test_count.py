import pytest
from datastructures.Stack.Stack import Stack

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_positive(input_data,expected):
    s = Stack()
    for i in range(0,input_data):
        s.push(i)
    assert s.count() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (100, 100)
                         ])

def test_pound(input_data,expected):
    s = Stack()
    for i in range(0,input_data):
        s.push(i)
    assert s.count() == expected