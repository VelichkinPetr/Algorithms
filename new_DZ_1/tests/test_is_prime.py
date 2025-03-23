import pytest
from new_DZ_1.is_prime import is_prime

@pytest.mark.parametrize('data,expected', [
    (5, True),
    (12, False),
    (19, True),
    (21, False),
    (51287, True)
])
def test_positive(data,expected):
    assert is_prime(data) == expected

@pytest.mark.parametrize('data,expected', [
    (0, False),
    (1, False),
    (-1, False),
    (2, True)
])
def test_bound(data,expected):
    assert is_prime(data) == expected

@pytest.mark.parametrize('data,expected', [
    ('', TypeError),
    ('2', TypeError),
    ('aaa', TypeError),
    ([2], TypeError)
])
def test_negative(data,expected):
    with pytest.raises(expected):
        is_prime(data)