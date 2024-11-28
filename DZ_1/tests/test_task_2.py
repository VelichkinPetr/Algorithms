import task_2

def test_type_input_not_int():
    numbers = ['1','2',3]
    assert task_2.min_frequent_elem(numbers) == []

def test_input_empty_list():
    numbers = []
    assert task_2.min_frequent_elem(numbers) == []

def test_input_zero_in_list():
    numbers = [0]
    assert task_2.min_frequent_elem(numbers) == []

def test_input_not_list():
    numbers = 1
    assert task_2.min_frequent_elem(numbers) == []

def test_one_elem_list():
    numbers = [7]
    assert task_2.min_frequent_elem(numbers) == 7

def test_one_negative_elem_list():
    numbers = [-7]
    assert task_2.min_frequent_elem(numbers) == []

def test_positive_int_list():
    numbers = [1,2,3,4,5,6]
    assert task_2.min_frequent_elem(numbers) == 1

def test_negative_int_list():
    numbers = [-1,-2,-3,-4,-5,-6]
    assert task_2.min_frequent_elem(numbers) == []

def test_min_numbers_not_in_allowed_range():
    numbers = [0, 1, 2, 2, 3, 3]
    assert task_2.min_frequent_elem(numbers) == []

def test_max_numbers_not_in_allowed_range():
    numbers = [1, 1, 3, 3, 5, 20001]
    assert task_2.min_frequent_elem(numbers) == []

def test_correct_input_list():
    numbers = [3, 1, 3, 4, 20000,4]
    assert task_2.min_frequent_elem(numbers) == 3

def test_ideal_input_list():
    numbers = [1,2,2,3,3,3,4,4,4,4]
    assert task_2.min_frequent_elem(numbers) == 4

def test_expected_input_list():
    numbers = [55 , 4 ,67, 4 ,8, 3 , 4 ,9, 55 , 3 ,1, 55 , 3]
    assert task_2.min_frequent_elem(numbers) == 3

def test_max_len_list():
    numbers = [i for i in range(10 ** 5 + 1)]
    assert task_2.min_frequent_elem(numbers) == []