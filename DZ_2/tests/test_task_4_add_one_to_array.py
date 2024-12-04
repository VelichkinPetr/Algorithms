import pytest
from DZ_2.task_4_add_one_to_array import add_one_to_array

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( [1,2,3,4,5,6], [1,2,3,4,5,7] ),
                             ( [1,2,3], [1,2,4] ),
                             ( [8], [9] ),
                             ( [i for i in range(1,10)]*9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 1,
                                                            2, 3, 4, 5, 6, 7, 8, 9, 1, 2,
                                                            3, 4, 5, 6, 7, 8, 9, 1, 2, 3,
                                                            4, 5, 6, 7, 8, 9, 1, 2, 3, 4,
                                                            5, 6, 7, 8, 9, 1, 2, 3, 4, 5,
                                                            6, 7, 8, 9, 1, 2, 3, 4, 5, 6,
                                                            7, 8, 9, 1, 2, 3, 4, 5, 6, 7,
                                                            8, 9, 1, 2, 3, 4, 5, 6, 7, 9,0] )
                                     ])
def test_positive(input_data,expected):
    assert add_one_to_array(input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( '', TypeError ),
                             ( [], ValueError ),
                             ( ['5',6,2,5,3], TypeError ),
                             ( [''], TypeError ),
                             ( [i for i in range(1,2)]*101, ValueError ),
                             ( [0] , ValueError ),
                             ( [1,2,3,4,10] , ValueError ),
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
        add_one_to_array(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( [9], [1,0] ),
                             ( [2], [3] ),
                             ( [2,0], [2,1] ),
                             ( [9,9,9,9], [1,0,0,0,0] ),
                             ( [i for i in range(9,10)]*100, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                         ])
def test_bound(input_data,expected):
    assert add_one_to_array(input_data) == expected