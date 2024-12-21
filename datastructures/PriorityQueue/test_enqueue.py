import pytest
from PriorityQueue import PriorityQueue, Task

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, ['1','2']),
                             (3, ['1','2','3']),
                             (4, ['1','2','3','4']),
                             (5, ['1','2','3','4','5'])
                         ])

def test_positive(input_data,expected):
    pq = PriorityQueue()
    for i in range(1,input_data+1):
        task = Task(f'{i}',i)
        pq.enqueue(task)
    assert pq.print_PriorityQueue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1])
                         ])

def test_bound(input_data,expected):
    pq = PriorityQueue()
    task = Task(input_data,input_data)
    pq.enqueue(task)
    assert pq.print_PriorityQueue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, AttributeError),
                             ('', TypeError),
                             ([], TypeError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        pq = PriorityQueue()
        task = Task('', input_data)
        pq.enqueue(input_data)