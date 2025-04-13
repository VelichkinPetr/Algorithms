import pytest
from new_DZ_4.RandomBag import RandomBag


@pytest.fixture(scope= 'session')
def RB():
    return RandomBag()

@pytest.mark.parametrize('data,expected',[
    (1,(5, [1, None, None, None, None], 1)),
    (2,(5, [1, 2, None, None, None], 2)),
    (3,(5, [1, 2, 3, None, None], 3)),
    (4,(5, [1, 2, 3, 4, None], 4))
])

def test_positive(RB,data,expected):
    RB.add(data)
    assert RB.get() == expected

@pytest.mark.parametrize('data,expected',[
    (5,(5, [1, 2, 3, 4, 5], 5)),
    (6,(8, [1, 2, 3, 4, 5, 6, None, None], 6))
])

def test_bound(RB,data,expected):
    RB.add(data)
    assert RB.get() == expected