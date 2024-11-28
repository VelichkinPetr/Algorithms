import mod_5_task_1

def test_type_input_not_int():
    n = '2'
    assert mod_5_task_1.factorial(n) == 0

def test_input_zero():
    n = 0
    assert mod_5_task_1.factorial(n) == 1

def test_input_one():
    n = 1
    assert mod_5_task_1.factorial(n) == 1

def test_input_max():
    n = 20
    assert mod_5_task_1.factorial(n) == 2432902008176640000

def test_input_more_max():
    n = 21
    assert mod_5_task_1.factorial(n) == 0

def test_input_negativ():
    n = -1
    assert mod_5_task_1.factorial(n) == 0

def test_input_normal():
    n = 11
    assert mod_5_task_1.factorial(n) == 39916800