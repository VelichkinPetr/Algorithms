import pytest
from datastructures.DeQueue.DeQueue import DeQueue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, 1),
                             (2, 2),
                             (3, 3),
                             (4, 4),
                             (5, 5)
                         ])

def test_positive(input_data,expected):
    dq = DeQueue()
    for i in range(1,input_data+1):
        dq.pushBack(i)
    assert dq.popBack() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, None)
                         ])

def test_bound(input_data,expected):
    dq = DeQueue()
    dq.pushBack(input_data)
    dq.popBack()
    assert dq.popBack() == expected