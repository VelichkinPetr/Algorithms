import pytest
from DZ_2.task_1_max_in_range import max_in_range
@pytest.mark.parametrize('input_data,expected',
                         [
                             (([-1,2,5,22,-8,12,3],2,6), (22,3,1)),
                             (([-1,-2,-5,-22,-8,-12,-3],4,6), (-3,6,2)),
                             (([1,2,5,22,8,12,3],1,2), (5,2,1)),
                             (([1],0,0), (1,0,0))
                         ])
def test_positive(input_data,expected):
    assert max_in_range(*input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             ((['-1',2,5,22,-8,12,3],2,6), TypeError),
                             (([-1,-2,-5,-22,-8,-12,-3],'4',6), TypeError),
                             (([1,2,5,22,8,12,3],1,'2'), TypeError),
                             (([],1,3), ValueError),
                             (([1,2,5,22,8,12,3],-1,3), ValueError),
                             (([1,2,5,22,8,12,3],1,-3), ValueError),
                             (([''],1,3), TypeError),
                             (([1,2,5,22,8,12,3],1,7), ValueError),
                             (([1,2,5,22,8,12,3],7,3), ValueError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     max_in_range(*input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             (([0],0,0), (0,0,0)),
                             (([1],0,0), (1,0,0)),
                             (([6,2,5,22,8,12,3],0,0), (6,0,0)),
                             (([6,2,5,22,8,12,3],6,6), (3,6,0))
                         ])
def test_bound(input_data,expected):
    assert max_in_range(*input_data) == expected