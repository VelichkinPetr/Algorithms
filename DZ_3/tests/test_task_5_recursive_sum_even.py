import pytest
from DZ_3.task_5_recursive_sum_even import recursive_sum_even

@pytest.mark.parametrize('input_data, expected',[
    ([1,2,3,4,5], 6),
    ([5,4,3,2,1], 6),
    ([1,-2,5,3,4], 2),
    ([-1,-2,-5,-3,-4], -6),
    ([-1,-2,2,-3,-4], -4),
])

def test_positive(input_data,expected):
    assert recursive_sum_even(input_data) == expected


@pytest.mark.parametrize('input_data,expected',
                         [
                             ([''], TypeError),
                             (['',1], TypeError),
                             ([-1,-2,'3',4,5], TypeError),
                             ('', IndexError),
                             (1, TypeError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     recursive_sum_even(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ([], 0),
                             ([1], 0),
                             ([0,0,0,0,0], 0),
                             ([1 for i in range(1,101)], 0),
                             ([2 for i in range(1,101)], 200)
                         ])
def test_bound(input_data,expected):
    assert recursive_sum_even(input_data) == expected