import pytest
from new_DZ_1.fast_power import fast_power

@pytest.mark.parametrize('data,expected', [
    ((2,5), 32),
    ((2,2), 4),
    ((-2,5), -32)
])
def test_positive(data,expected):
    assert fast_power(*data) == expected

@pytest.mark.parametrize('data,expected', [
    ((0,5), 0),
    ((1,10), 1),
    ((-1,9), -1)
])
def test_bound(data,expected):
    assert fast_power(*data) == expected

@pytest.mark.parametrize('data,expected', [
    (('',5), TypeError),
    (('2',2), TypeError),
    ((-2,'5'), TypeError),
    ((-2,'dfadfda'), TypeError),
    (('a','b'), TypeError),
    (([-2],5), TypeError)
])
def test_negative(data,expected):
    with pytest.raises(expected):
        fast_power(*data)