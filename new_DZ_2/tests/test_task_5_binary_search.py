import pytest
from new_DZ_2.task_5_binary_search import search_binary

@pytest.mark.parametrize('data,expected', [

    (([1,2,3,4,5,6,7,8,9], 2), 1),
    (([1,2,3,4,5,6,7,8,9], 3), 2),
    (([1,2,3,4,5,6,7,8,9], 4), 3),
    (([1,2,3,4,5,6,7,8,9], 5), 4),
    (([1,2,3,4,5,6,7,8,9], 6), 5),
    (([1,2,3,4,5,6,7,8,9], 7), 6),
    (([1,2,3,4,5,6,7,8,9], 8), 7),

])
def test_positive(data,expected):
    assert search_binary(*data) == expected

@pytest.mark.parametrize('data,expected', [
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 0), -1),
    (([1,2,3,4,5,6,7,8,9], 1), 0),
    (([1,2,3,4,5,6,7,8,9], 9), 8),
    (([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1),
])
def test_bound(data,expected):
    assert search_binary(*data) == expected

@pytest.mark.parametrize('data,expected', [
    (('',5), TypeError),
    (('2',2), TypeError),
    ((-2,'5'), TypeError),
    ((-2,'dfadfda'), TypeError),
    (('a','b'), TypeError),
    (([-2],'5'), TypeError)
])
def test_negative(data,expected):
    with pytest.raises(expected):
        search_binary(*data)