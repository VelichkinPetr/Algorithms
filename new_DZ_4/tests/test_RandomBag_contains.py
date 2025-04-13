import pytest
from new_DZ_4.RandomBag import RandomBag


@pytest.fixture(scope= 'session')
def RB():
    data = RandomBag()

    for i in range(1, 6, 1):
        data.add(i)

    return data

@pytest.mark.parametrize('data,expected',[
    (1,True),
    (2,True),
    (3,True),
    (4,True),
    (5,True)
])

def test_positive(RB,data,expected):
    assert RB.contains(data) == expected

@pytest.mark.parametrize('data,expected',[
    (6,False),
    (0,False),
    (-1, False),
    (100, False),
    (-100, False)
])

def test_bound(RB,data,expected):
    assert RB.contains(data) == expected