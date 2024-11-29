import pytest
from DZ_1.mod_5_task_4 import is_palindrome

def test_type_input_not_int():
    x = '2'
    with pytest.raises(TypeError): is_palindrome(x)

def test_input_zero():
    x = 0
    assert is_palindrome(x) == True

def test_input_one():
    x = 1
    assert is_palindrome(x) == True

def test_input_minus_one():
    x = -1
    assert is_palindrome(x) == True

def test_input_positive():
    x = 121
    assert is_palindrome(x) == True

def test_input_negative():
    x = -121
    assert is_palindrome(x) == False

def test_input_len_is_2_negative():
    x = 10
    assert is_palindrome(x) == False

def test_input_len_is_2_positive():
    x = 11
    assert is_palindrome(x) == True

def test_input_len_is_12_positive():
    x = 123456654321
    assert is_palindrome(x) == True

def test_input_len_is_13_positive():
    x = 1234567654321
    assert is_palindrome(x) == True

def test_input_len_is_12_negative():
    x = 125456654321
    assert is_palindrome(x) == False

def test_input_len_is_13_negative():
    x = 1234557654321
    assert is_palindrome(x) == False