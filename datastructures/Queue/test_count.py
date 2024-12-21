import pytest
from Queue import Queue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_positive(input_data,expected):
    q = Queue()
    for i in range(0, input_data):
        q.enqueue(i)
    assert q.count() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (100, 100)
                         ])

def test_bound(input_data,expected):
    q = Queue()
    for i in range(0, input_data):
        q.enqueue(i)
    assert q.count() == expected