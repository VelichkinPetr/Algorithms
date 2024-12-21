import pytest
from DeQueue import DeQueue

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, [2,1]),
                             (3, [3,2,1]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1])
                         ])

def test_positive(input_data,expected):
    dq = DeQueue()
    for i in range(1,input_data+1):
        dq.pushFront(i)
    assert dq.print_DeQueue() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             ('', ['']),
                             ([], [[]])
                         ])

def test_bound(input_data,expected):
    dq = DeQueue()
    dq.pushFront(input_data)
    assert dq.print_DeQueue() == expected