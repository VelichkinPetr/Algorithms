import pytest
from Stack import Stack

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_is_empty(input_data,expected):
    s = Stack()
    for i in range(0,input_data):
        s.push(i)
    assert s.is_empty() == expected