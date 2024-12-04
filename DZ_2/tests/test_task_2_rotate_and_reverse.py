import pytest
from DZ_2.task_2_rotate_and_reverse import rotate_and_reverse

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( ([1,2,3,4,5,6],2), [4,3,2,1,6,5] ),
                             ( ([5,6,2,5,3],3), [6,5,3,5,2] ),
                             ( ([5,6,2,-5,3],3), [6,5,3,-5,2] ),
                             ( (['5',6,2,-5,3],3), [6,'5',3,-5,2] ),
                             ( ([2,'3',7, ],2), [2, 7, '3'] ),
                         ])
def test_positive(input_data,expected):
    assert rotate_and_reverse(*input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( ('',2), TypeError ),
                             ( ([],5), ValueError ),
                             ( ([5,6,2,5,3],-3), ValueError ),
                             ( ([5,6,2,5,3],'3'), TypeError )
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
        rotate_and_reverse(*input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( ([0],0), [0] ),
                             ( ([''],5), [''] ),
                             ( ([1],5), [1] ),
                             ( ([6,2,5,22,8,12,3],0), [3,12,8,22,5,2,6] ),
                             ( ([6,2,5,22],4), [22,5,2,6]),
                             ( ([6,2,5,22],5), [5,2,6,22]),
                             ( ([6,2,5,22],13), [5,2,6,22])
                         ])
def test_bound(input_data,expected):
    assert rotate_and_reverse(*input_data) == expected