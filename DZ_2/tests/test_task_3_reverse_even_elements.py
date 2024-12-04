import pytest
from DZ_2.task_3_reverse_even_elements import reverse_even_elements

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( [1,2,3,4,5,6], [1,6,3,4,5,2] ),
                             ( [1,2,3,5,5,6], [1,6,3,5,5,2] ),
                             ( [1,2,3,5,5,7], [1,2,3,5,5,7] ),
                             ( [2,5,7,8,5,4,7,6], [6,5,7,4,5,8,7,2] )
                         ])
def test_positive(input_data,expected):
    assert reverse_even_elements(input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( '', TypeError ),
                             ( [], ValueError ),
                             ( ['5',6,2,5,3], TypeError ),
                             ( [''], TypeError )
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
        reverse_even_elements(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ([1],[1]),
                             ([2],[2]),
                             ([2,4],[4,2]),
                             ([3,5,4,5],[3,5,4,5]),
                             ( [2,6,4], [4,6,2] )
                         ])
def test_bound(input_data,expected):
    assert reverse_even_elements(input_data) == expected