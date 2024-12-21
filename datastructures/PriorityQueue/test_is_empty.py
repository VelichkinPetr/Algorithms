import pytest
from PriorityQueue import PriorityQueue, Task

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_positive(input_data,expected):
    pq = PriorityQueue()
    for i in range(1,input_data+1):
        task = Task(f'{i}',i)
        pq.enqueue(task)
    assert pq.is_empty() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False)
                         ])

def test_bound(input_data,expected):
    pq = PriorityQueue()
    for i in range(1, input_data + 1):
        task = Task(f'{i}', i)
        pq.enqueue(task)
    assert pq.is_empty() == expected