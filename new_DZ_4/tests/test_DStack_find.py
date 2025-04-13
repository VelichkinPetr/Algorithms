import pytest
from new_DZ_4.DStack import DStack


@pytest.fixture(scope= 'session')
def dynamic_stack():
    data = DStack()

    for i in range(1,12,1):
        data.push(i)

    return data

@pytest.mark.parametrize('data, expected',[
    (11,10),
    (10,9),
    (9,8),
    (8,7),
    (7,6),
    (6,5),
    (5,4),
    (4,3),
    (3,2),
    (2,1),
    (1,0)
])

def test_positive(dynamic_stack,data,expected):
    assert dynamic_stack.find(data) == expected

@pytest.mark.parametrize('data, expected',[
    (12,-1),
    (100,-1),
    (-1111,-1)
])

def test_bound(dynamic_stack,data,expected):
    assert dynamic_stack.find(data) == expected