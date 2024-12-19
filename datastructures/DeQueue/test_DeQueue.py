import pytest
from DeQueue import DeQueue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [2,1]),
                             (3, [3,2,1]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1])
                         ])

def test_pushFront(input_data,expected):
    dq = DeQueue()
    for i in range(1,input_data+1):
        dq.pushFront(i)
    assert dq.print_DeQueue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [1, 2]),
                             (3, [1, 2, 3]),
                             (4, [1, 2, 3, 4]),
                             (5, [1, 2, 3, 4, 5])
                         ])

def test_pushBack(input_data,expected):
    dq = DeQueue()
    for i in range(1,input_data+1):
        dq.pushBack(i)
    assert dq.print_DeQueue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 1),
                             (3, 1),
                             (4, 1),
                             (5, 1)
                         ])

def test_popFront(input_data,expected):
    dq = DeQueue()
    for i in range(1,input_data+1):
        dq.pushBack(i)
    assert dq.popFront() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_popFront_bound(input_data,expected):
    dq = DeQueue()
    dq.pushFront(input_data)
    dq.popFront()
    assert dq.popFront() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 2),
                             (3, 3),
                             (4, 4),
                             (5, 5)
                         ])

def test_popBack(input_data,expected):
    dq = DeQueue()
    for i in range(1,input_data+1):
        dq.pushBack(i)
    assert dq.popBack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_popBack_bound(input_data,expected):
    dq = DeQueue()
    dq.pushBack(input_data)
    dq.popBack()
    assert dq.popBack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 2),
                             (3, 3),
                             (4, 4),
                             (5, 5)
                         ])

def test_peekBack(input_data,expected):
    dq = DeQueue()
    for i in range(1, input_data + 1):
        dq.pushBack(i)
    assert dq.peekBack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_peekBack_bound(input_data,expected):
    dq = DeQueue()
    dq.pushBack(input_data)
    dq.popBack()
    assert dq.peekBack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 1),
                             (3, 1),
                             (4, 1),
                             (5, 1)
                         ])

def test_peekFront(input_data,expected):
    dq = DeQueue()
    for i in range(1, input_data + 1):
        dq.pushBack(i)
    assert dq.peekFront() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_peekFront_bound(input_data,expected):
    dq = DeQueue()
    dq.pushBack(input_data)
    dq.popBack()
    assert dq.peekFront() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_is_empty(input_data,expected):
    dq = DeQueue()
    for i in range(0,input_data):
        dq.pushFront(i)
    assert dq.is_empty() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_count(input_data,expected):
    dq = DeQueue()
    for i in range(0, input_data):
        dq.pushFront(i)
    assert dq.count() == expected