import pytest
from DZ_3.task_9_sum_of_digits import sum_of_digits

@pytest.mark.parametrize('input_data, expected',
                         [
                             (10,1),
                             (13,4),
                             (234, 9),
                             (12345, 15)
                         ])

def test_positive(input_data,expected):
    assert sum_of_digits(input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [

                             ([1], TypeError),
                             ([''], TypeError),
                             ([], TypeError),
                             ('', TypeError),
                             (-1, ValueError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     sum_of_digits(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             (0, 0),
                             (2, 2),
                             (0000, 0),
                             (11111, 5)
                         ])
def test_bound(input_data,expected):
    assert sum_of_digits(input_data) == expected