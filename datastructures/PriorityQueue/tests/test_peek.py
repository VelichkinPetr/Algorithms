import pytest
from datastructures.PriorityQueue.PriorityQueue import PriorityQueue, Task

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, '1'),
                             (2, '2'),
                             (3, '3'),
                             (4, '4'),
                             (5, '5')
                         ])

def test_positive_up(input_data,expected):
    pq = PriorityQueue()
    for i in range(1, input_data + 1):
        task = Task(f'{i}', i)
        pq.enqueue(task)
    assert pq.peek(order_by=lambda x,y: x>y) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, '1'),
                             (2, '1'),
                             (3, '1'),
                             (4, '1'),
                             (5, '1')
                         ])

def test_positive_down(input_data,expected):
    pq = PriorityQueue()
    for i in range(1, input_data + 1):
        task = Task(f'{i}', i)
        pq.enqueue(task)
    assert pq.peek(order_by=lambda x,y: x<y) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_bound_up(input_data,expected):
    pq = PriorityQueue()
    task = Task(f'{input_data}', input_data)
    pq.enqueue(task)
    pq.dequeue(order_by=lambda x, y: x > y)
    assert pq.peek(order_by=lambda x,y: x>y) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_bound_down(input_data,expected):
    pq = PriorityQueue()
    task = Task(f'{input_data}', input_data)
    pq.enqueue(task)
    pq.dequeue(order_by=lambda x, y: x < y)
    assert pq.peek(order_by=lambda x,y: x<y) == expected