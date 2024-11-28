import task_3

def test_type_input_not_int():
    nums = ['1','2',3]
    target = 3
    assert task_3.indexes_elements_get_target_sum(nums,target) == []

def test_target_not_int():
    nums = [1, 2, 3]
    target = '3'
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_input_empty_list():
    nums = []
    target = 3
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_zero_target():
    nums = [1,2,2]
    target = 0
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_target_not_in_list():
    nums = [0,0,0]
    target = 3
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_nums_not_list():
    nums = 3
    target = 3
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_less_min_len_list():
    nums = [2]
    target = 5
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_min_len_list():
    nums = [2,3]
    target = 5
    assert task_3.indexes_elements_get_target_sum(nums, target) == [0,1]

def test_max_len_list():
    nums = [i for i in range(104)]
    target = 5
    assert task_3.indexes_elements_get_target_sum(nums, target) == [0,5]

def test_len_more_max():
    nums = [i for i in range(105)]
    target = 5
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_target_negative_list_positive():
    nums = [1,3,5,2]
    target = -5
    assert task_3.indexes_elements_get_target_sum(nums, target) == []

def test_target_negative_list_mix():
    nums = [1,-3,5,-2]
    target = -5
    assert task_3.indexes_elements_get_target_sum(nums, target) == [1,3]

def test_min_target_negative_list_mix():
    nums = [-107,-3,5,-2]
    target = -109
    assert task_3.indexes_elements_get_target_sum(nums, target) == [0,3]

def test_min_target_negative_list_mix():
    nums = [-107,-3,99,-2,10]
    target = 109
    assert task_3.indexes_elements_get_target_sum(nums, target) == [2,4]