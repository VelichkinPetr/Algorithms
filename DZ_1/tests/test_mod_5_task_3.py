import pytest
from DZ_1.mod_5_task_3 import count_ones

def test_type_input_not_int():
    n = '2'
    with pytest.raises(TypeError): count_ones(n)

def test_input_zero():
    n = 0
    assert count_ones(n) == 0

def test_input_one():
    n = 1
    assert count_ones(n) == 1

def test_input_positive_even():
    n = 1024
    assert count_ones(n) == 1

def test_input_positive_odd():
    n = 1023
    assert count_ones(n) == 10

def test_input_negativ():
    n = -1
    with pytest.raises(ValueError): count_ones(n)