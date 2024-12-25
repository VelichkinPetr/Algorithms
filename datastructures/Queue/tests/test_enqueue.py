import pytest
from datastructures.Queue.Queue import Queue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, [1,2]),
                             (3, [1,2,3]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5])
                         ])

def test_positive(input_data,expected):
    q = Queue()
    for i in range(1,input_data+1):
        q.enqueue(i)
    assert q.print_Queue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             ('', ['']),
                             ([], [[]])
                         ])

def test_bound(input_data,expected):
    q = Queue()
    q.enqueue(input_data)
    assert q.print_Queue() == expected