import pytest
from datastructures.DeQueue import DeQueue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, [1, 2]),
                             (3, [1, 2, 3]),
                             (4, [1, 2, 3, 4]),
                             (5, [1, 2, 3, 4, 5])
                         ])

def test_positive(input_data,expected):
    dq = DeQueue.DeQueue()
    for i in range(1,input_data+1):
        dq.pushBack(i)
    assert dq.print_DeQueue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             ('', ['']),
                             ([], [[]])
                         ])

def test_bound(input_data,expected):
    dq = DeQueue.DeQueue()
    dq.pushBack(input_data)
    assert dq.print_DeQueue() == expected