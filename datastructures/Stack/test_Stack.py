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

def test_push(input_data,expected):
    s = Stack()
    for i in range(1,input_data+1):
        s.push(i)
    assert s.print_Stack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 2),
                             (2, 4),
                             (3, 6),
                             (4, 8),
                             (5, 10)
                         ])

def test_pop(input_data,expected):
    s = Stack()
    for i in range(1,input_data+1):
        s.push(i*2)
    assert s.pop() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_pop_bound(input_data,expected):
    s = Stack()
    s.push(input_data)
    s.pop()
    assert s.pop() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 2),
                             (2, 4),
                             (3, 6),
                             (4, 8),
                             (5, 10)
                         ])

def test_peek(input_data,expected):
    s = Stack()
    for i in range(1,input_data+1):
        (s.push(i*2))
    assert s.peek() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_peek_bound(input_data,expected):
    s = Stack()
    s.push(input_data)
    s.pop()
    assert s.peek() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_is_empty(input_data,expected):
    s = Stack()
    for i in range(0,input_data):
        s.push(i)
    assert s.is_empty() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_count(input_data,expected):
    s = Stack()
    for i in range(0,input_data):
        s.push(i)
    assert s.count() == expected