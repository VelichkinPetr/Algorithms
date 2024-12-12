import pytest
from DZ_3.task_8_fibonacci import fibonacci

@pytest.mark.parametrize('input_data, expected',
                         [
                             (10,55),
                             (13,233),
                             (3, 2)
                         ])

def test_positive(input_data,expected):
    assert fibonacci(input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [

                             ([1], TypeError),
                             ([''], TypeError),
                             ([], TypeError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     fibonacci(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             (0, 0),
                             (1, 1),
                             (2, 1),
                             (-1, 0),
                             (20, 6765)
                         ])
def test_bound(input_data,expected):
    assert fibonacci(input_data) == expected