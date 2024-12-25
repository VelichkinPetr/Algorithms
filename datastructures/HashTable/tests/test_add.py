import pytest
from datastructures.HashTable.HashTable import HashMap

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, 2),
                             (3, 3),
                             (4, 4),
                             (5, 5)
                         ])

def test_positive(input_data,expected):
    map = HashMap()
    for i in range(1,input_data+1):
        map.add(f'*{i}',i)
    assert map.count == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ([], TypeError),
                             ([3], TypeError),
                             (['4'], TypeError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        map = HashMap()
        map.add(input_data,input_data)

