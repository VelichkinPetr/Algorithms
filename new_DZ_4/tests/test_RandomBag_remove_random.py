import pytest
from new_DZ_4.RandomBag import RandomBag


@pytest.fixture(scope= 'function')
def RB():
    return RandomBag()

def test_negative(RB):
    with pytest.raises(ValueError):
        RB.remove_random()

@pytest.mark.parametrize('data,expected',[
    (1,False),
    (2,False),
    (3,False),
    (4,False),
    (5,False)
])

def test_positive(RB,data,expected):
    for i in range(1,data+1):
        RB.add(i)

    assert RB.contains(RB.remove_random()) == expected
