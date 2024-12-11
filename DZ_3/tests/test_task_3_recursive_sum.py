import pytest
from DZ_3.task_3_recursive_sum import recursive_sum

@pytest.mark.parametrize('input_data, expected',[
    ([1,2,3,4,5], 15),
    ([-1,-2,3,4,5], 9),
    ([-1,-2,-3,-4,-5], -15)
])

def test_positive(input_data,expected):
    assert recursive_sum(input_data) == expected


@pytest.mark.parametrize('input_data,expected',
                         [
                             ([''], TypeError),
                             ([-1,-2,'3',4,5], TypeError),
                             ('', IndexError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     recursive_sum(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ([], 0),
                             ([1], 1),
                             ([0,0,0,0,0], 0),
                             ([1 for i in range(1,101)], 100)
                         ])
def test_bound(input_data,expected):
    assert recursive_sum(input_data) == expected