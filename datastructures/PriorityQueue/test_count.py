import pytest
from PriorityQueue import PriorityQueue, Task

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_positive(input_data,expected):
    pq = PriorityQueue()
    for i in range(1,input_data+1):
        task = Task(f'{i}',i)
        pq.enqueue(task)
    assert pq.count() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (100, 100)
                         ])

def test_bound(input_data,expected):
    pq = PriorityQueue()
    for i in range(1,input_data+1):
        task = Task(f'{i}',i)
        pq.enqueue(task)
    assert pq.count() == expected