import pytest
from DZ_1.mod_5_task_1 import factorial

def test_type_input_not_int():
    n = '2'
    with pytest.raises(TypeError): factorial(n)

def test_input_zero():
    n = 0
    assert factorial(n) == 1

def test_input_one():
    n = 1
    assert factorial(n) == 1

def test_input_max():
    n = 20
    assert factorial(n) == 2432902008176640000

def test_input_more_max():
    n = 21
    with pytest.raises(ValueError): factorial(n)

def test_input_negativ():
    n = -1
    with pytest.raises(ValueError): factorial(n)

def test_input_normal():
    n = 11
    assert factorial(n) == 39916800