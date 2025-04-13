import pytest
from new_DZ_4.RandomBag import RandomBag


@pytest.fixture(scope= 'session')
def RB():

    return RandomBag()

def test_negative(RB):
    with pytest.raises(ValueError):
        RB.get_random()

@pytest.mark.parametrize('data,expected',[
    (1,True),
    (5,True),
    (1000,True)
])

def test_positive(RB,data,expected):
    for i in range(data):
        RB.add(i)
        assert RB.contains(RB.get_random()) == True

