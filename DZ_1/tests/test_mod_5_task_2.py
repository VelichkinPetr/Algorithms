import pytest
from DZ_1.mod_5_task_2 import fibonacci

def test_type_input_not_int():
    n = '2'
    with pytest.raises(TypeError): fibonacci(n)

def test_input_zero():
    n = 0
    assert fibonacci(n) == [0]

def test_input_one():
    n = 1
    assert fibonacci(n) == [0,1]

def test_input_two():
    n = 2
    assert fibonacci(n) == [0,1,1]

def test_input_ten():
    n = 10
    assert fibonacci(n) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_input_negativ():
    n = -1
    with pytest.raises(ValueError): fibonacci(n)
