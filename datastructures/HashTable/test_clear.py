import pytest
from HashTable import HashMap

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 0),
                             (3, 0),
                             (4, 0),
                             (5, 0),
                             (100, 0)
                         ])

def test_positive(input_data,expected):
    map = HashMap()
    for i in range(1,input_data+1):
        map.add(i,f'*{i}')
    map.clear()
    assert map.count == expected