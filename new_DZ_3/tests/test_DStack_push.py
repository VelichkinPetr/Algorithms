import pytest
from new_DZ_3.DStack import DStack


@pytest.fixture(scope= 'session')
def dynamic_stack():
    return DStack()

@pytest.mark.parametrize('data,expected',[
    (1,(10, [1, None, None, None, None, None, None, None, None, None], 1)),
    (2,(10, [1, 2, None, None, None, None, None, None, None, None], 2)),
    (3,(10, [1, 2, 3, None, None, None, None, None, None, None], 3)),
    (4,(10, [1, 2, 3, 4, None, None, None, None, None, None], 4)),
    (5,(10, [1, 2, 3, 4, 5, None, None, None, None, None], 5)),
    (6,(10, [1, 2, 3, 4, 5, 6, None, None, None, None], 6)),
    (7,(10, [1, 2, 3, 4, 5, 6, 7, None, None, None], 7)),
    (8,(10, [1, 2, 3, 4, 5, 6, 7, 8, None, None], 8))
])

def test_positive(dynamic_stack,data,expected):
    dynamic_stack.push(data)
    assert dynamic_stack.get() == expected

@pytest.mark.parametrize('data,expected',[
    (9, (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, None], 9)),
    (10,(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)),
    (11,(16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None, None, None], 11)),
    (12,(16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, None, None, None], 12))
])

def test_bound(dynamic_stack,data,expected):
    dynamic_stack.push(data)
    assert dynamic_stack.get() == expected