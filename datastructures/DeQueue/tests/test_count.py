import pytest
from datastructures.DeQueue.DeQueue import DeQueue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 2),
                             (3, 3),
                             (4, 4)
                         ])

def test_positive(input_data,expected):
    dq = DeQueue()
    for i in range(0, input_data):
        dq.pushFront(i)
    assert dq.count() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, 0),
                             (1, 1),
                             (100, 100)
                         ])

def test_bound(input_data,expected):
    dq = DeQueue()
    for i in range(0, input_data):
        dq.pushFront(i)
    assert dq.count() == expected