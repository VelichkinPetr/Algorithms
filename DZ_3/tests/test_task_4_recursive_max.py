import pytest
from DZ_3.task_4_recursive_max import recursive_max

@pytest.mark.parametrize('input_data, expected',[
    ([1,2,3,4,5], 5),
    ([5,4,3,2,1], 5),
    ([1,2,5,3,4], 5),
    ([-1,-2,-5,-3,-4], -1),
    ([-1,-2,0,-3,-4], 0),
])

def test_positive(input_data,expected):
    assert recursive_max(input_data) == expected


@pytest.mark.parametrize('input_data,expected',
                         [
                             ([''], TypeError),
                             (['',1], TypeError),
                             ([-1,-2,'3',4,5], TypeError),
                             ('', TypeError),
                             (1, TypeError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     recursive_max(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ([], 0),
                             ([1], 1),
                             ([0,0,0,0,0], 0),
                             ([i for i in range(1,101)], 100)
                         ])
def test_bound(input_data,expected):
    assert recursive_max(input_data) == expected