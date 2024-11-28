import mod_5_task_2

def test_type_input_not_int():
    n = '2'
    assert mod_5_task_2.fibonacci(n) == []

def test_input_zero():
    n = 0
    assert mod_5_task_2.fibonacci(n) == [0]

def test_input_one():
    n = 1
    assert mod_5_task_2.fibonacci(n) == [0,1]

def test_input_two():
    n = 2
    assert mod_5_task_2.fibonacci(n) == [0,1,1]

def test_input_ten():
    n = 10
    assert mod_5_task_2.fibonacci(n) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_input_negativ():
    n = -1
    assert mod_5_task_2.fibonacci(n) == []

