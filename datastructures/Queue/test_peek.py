import pytest
from Queue import Queue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 1),
                             (3, 1),
                             (4, 1),
                             (5, 1)
                         ])

def test_positive(input_data,expected):
    q = Queue()
    for i in range(1, input_data + 1):
        q.enqueue(i)
    assert q.peek() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_bound(input_data,expected):
    q = Queue()
    q.enqueue(input_data)
    q.dequeue()
    assert q.peek() == expected