import pytest
from new_DZ_4.RandomBag import RandomBag


@pytest.fixture(scope= 'function')
def RB():
    return RandomBag()

@pytest.mark.parametrize('data,expected',[
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
])

def test_positive(RB,data,expected):
    for i in range(1,data+1):
        RB.add(1)
    assert RB.count_item(1) == expected

@pytest.mark.parametrize('data,expected',[
    (1,0)
])

def test_bound(RB,data,expected):
    assert RB.count_item(data) == expected