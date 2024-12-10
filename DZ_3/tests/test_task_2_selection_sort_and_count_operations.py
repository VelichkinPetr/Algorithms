import pytest
from DZ_3.task_2_selection_sort_and_count_operations import selection_sort_and_count_operations

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( ([-1,2,5,22,-8,12,3],lambda x,y: x<y), ([22, 12, 5, 3, 2, -1, -8], 9, 6) ),
                             ( ([-1,2,5,22,-8,12,3],lambda x,y: x>y), ([-8, -1, 2, 3, 5, 12, 22], 5, 6) )
                         ])
def test_positive(input_data,expected):
    assert selection_sort_and_count_operations(*input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             ((['-1',2,5,22,-8,12,3],lambda x,y: x<y), TypeError),
                             (([1,2,5,22,8,12,3],'2'), TypeError),
                             (('',lambda x,y: x<y), TypeError),
                             (([1,2,5,22,8,12,3],1), TypeError),
                             (([''],lambda x,y: x<y), TypeError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     selection_sort_and_count_operations(*input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             (([], lambda x, y: x < y), ([], 0, 0)),
                             (([3, 3, 3, 3, 3],lambda x, y: x < y), ([3, 3, 3, 3, 3], 0, 4)),
                             (([1, 2, 3, 4, 5], lambda x, y: x < y), ([5, 4, 3, 2, 1], 6, 4))
                         ])
def test_bound(input_data,expected):
    assert selection_sort_and_count_operations(*input_data) == expected