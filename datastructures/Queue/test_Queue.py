import pytest
from Queue import Queue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [1,2]),
                             (3, [1,2,3]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5])
                         ])

def test_enqueue(input_data,expected):
    q = Queue()
    for i in range(1,input_data+1):
        q.enqueue(i)
    assert q.print_Queue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 2),
                             (2, 2),
                             (3, 2),
                             (4, 2),
                             (5, 2)
                         ])

def test_dequeue(input_data,expected):
    q = Queue()
    for i in range(1,input_data+1):
        q.enqueue(i*2)
    assert q.dequeue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_dequeue_bound(input_data,expected):
    q = Queue()
    q.enqueue(input_data)
    q.dequeue()
    assert q.dequeue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 2),
                             (2, 2),
                             (3, 2),
                             (4, 2),
                             (5, 2)
                         ])

def test_peek(input_data,expected):
    q = Queue()
    for i in range(1, input_data + 1):
        q.enqueue(i * 2)
    assert q.peek() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_peek_bound(input_data,expected):
    q = Queue()
    q.enqueue(input_data)
    q.dequeue()
    assert q.peek() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_is_empty(input_data,expected):
    q = Queue()
    for i in range(0,input_data):
        q.enqueue(i)
    assert q.is_empty() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_count(input_data,expected):
    q = Queue()
    for i in range(0, input_data):
        q.enqueue(i)
    assert q.count() == expected