import pytest
from DZ_1.task_1 import sum_even_numbers_in_list

def test_type_input_not_int():
    numbers = ['1','2',3]
    with pytest.raises(TypeError): sum_even_numbers_in_list(numbers)

def test_input_empty_list():
    numbers = []
    assert sum_even_numbers_in_list(numbers) == 0

def test_input_zero_in_list():
    numbers = [0]
    assert sum_even_numbers_in_list(numbers) == 0

def test_input_not_list():
    numbers = 1
    with pytest.raises(TypeError): sum_even_numbers_in_list(numbers)

def test_one_odd_elem_list():
    numbers = [1]
    assert sum_even_numbers_in_list(numbers) == 0

def test_one_even_elem_list():
    numbers = [2]
    assert sum_even_numbers_in_list(numbers) == 2

def test_one_negative_elem_list():
    numbers = [-2]
    assert sum_even_numbers_in_list(numbers) == 1

def test_positive_int_list():
    numbers = [1,2,3,4,5,6]
    assert sum_even_numbers_in_list(numbers) == 12

def test_negative_int_list():
    numbers = [-1,-2,-3,-4,-5,-6]
    assert sum_even_numbers_in_list(numbers) == 1

def test_min_numbers_not_in_allowed_range():
    numbers = [-20001, 1, -3, 4, -5, 20]
    with pytest.raises(ValueError): sum_even_numbers_in_list(numbers)

def test_max_numbers_not_in_allowed_range():
    numbers = [9, 1, -3, 4, -5, 20001]
    with pytest.raises(ValueError): sum_even_numbers_in_list(numbers)

def test_correct_input_list():
    numbers = [-20000, 1, -3, 4, -5, 20000]
    assert sum_even_numbers_in_list(numbers) == 4

def test_max_len_list():
    numbers = [i for i in range(10 ** 5 + 1)]
    with pytest.raises(ValueError): sum_even_numbers_in_list(numbers)