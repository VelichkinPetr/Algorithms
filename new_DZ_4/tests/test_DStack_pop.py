import pytest
from new_DZ_4.DStack import DStack


@pytest.fixture(scope= 'session')
def dynamic_stack():
    data = DStack()

    for i in range(1,12,1):
        data.push(i)

    return data

@pytest.mark.parametrize('expected',[
    11,
    10,
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1

])

def test_positive(dynamic_stack,expected):
    print(dynamic_stack.get())
    assert dynamic_stack.pop() == expected

@pytest.mark.parametrize('expected',[
    None,
    None
])

def test_bound(dynamic_stack,expected):
    print(dynamic_stack.get())
    assert dynamic_stack.pop() == expected