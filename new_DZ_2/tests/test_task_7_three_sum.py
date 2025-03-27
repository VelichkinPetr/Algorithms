import pytest
from new_DZ_2.task_7_three_sum import three_sum

@pytest.mark.parametrize('data,expected', [

    ( [-1, 0, 1, 2, -1, -4] ,  [[-1, -1, 2], [-1, 0, 1]]),
    ( [-1, 0, -1, 2, -1, -4] ,  [[-1, -1, 2]]),
    ( [-2, 0, 1, -2, -1, 4] ,  [[-2, -2, 4], [-1, 0, 1]]),
    ( [-2, 0, -1, -2, -1, 4] ,  [[-2, -2, 4]]),

])
def test_positive(data,expected):
    assert three_sum(data) == expected

@pytest.mark.parametrize('data,expected', [
    ( [] ,  [] ),
    (['44'], [] ),
    (['44','2','2'], [] ),
    ([['44','2'],['2'],['2']], [])
])
def test_bound(data,expected):
    assert three_sum(data) == expected

@pytest.mark.parametrize('data,expected', [
    ('', AttributeError),
    (2, AttributeError),
    ('dfadfda', AttributeError),
    (['44','2',2], TypeError),
    (['44',['2','2']], TypeError)
])
def test_negative(data,expected):
    with pytest.raises(expected):
        three_sum(data)