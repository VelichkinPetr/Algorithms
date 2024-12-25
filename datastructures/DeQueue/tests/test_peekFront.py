import pytest
from datastructures.DeQueue.DeQueue import (DeQueue)

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 1),
                             (3, 1),
                             (4, 1),
                             (5, 1)
                         ])

def test_positive(input_data,expected):
    dq = DeQueue()
    for i in range(1, input_data + 1):
        dq.pushBack(i)
    assert dq.peekFront() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_bound(input_data,expected):
    dq = DeQueue()
    dq.pushBack(input_data)
    dq.popBack()
    assert dq.peekFront() == expected