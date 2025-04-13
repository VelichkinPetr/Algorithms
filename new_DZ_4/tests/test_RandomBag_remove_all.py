import pytest
from new_DZ_4.RandomBag import RandomBag


@pytest.fixture(scope= 'function')
def RB():
    return RandomBag()


@pytest.mark.parametrize('data,expected',[
    (1,(1,(5, [2, None, None, None, None], 1))),
    (2,(2,(5, [2, 2, None, None, None], 2))),
    (3,(3,(8, [2, 2, 2, None, None, None, None, None], 3))),
    (4,(4,(8, [2, 2, 2, 2, None, None, None, None], 4))),
    (5,(5,(13, [2, 2, 2, 2, 2, None, None, None, None, None, None, None, None], 5)))
])

def test_positive(RB,data,expected):
    for i in range(1,data+1):
        RB.add(1)
        RB.add(2)
    assert (RB.remove_all(1) == expected[0] and RB.get() == expected[1])
