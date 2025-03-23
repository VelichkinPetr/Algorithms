import pytest
from new_DZ_1.gcd import gcd

@pytest.mark.parametrize('data,expected', [
    ((64,48), 16),
    ((111,432), 3),
    ((661,113), 1),
    ((220,600), 20)
])
def test_positive(data,expected):
    assert gcd(*data) == expected

@pytest.mark.parametrize('data,expected', [
    ((0,5), 5),
    ((12,0), 12),
    ((-12,33), 3),
    ((12,-33), 3),
    ((-12,-33), 3)
])
def test_bound(data,expected):
    assert gcd(*data) == expected

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
        gcd(*data)