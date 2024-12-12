import pytest
from DZ_3.task_7_is_palindrome import is_palindrome

@pytest.mark.parametrize('input_data, expected',
                         [
                             ('123321',True),
                             ('1234321',True),
                             ('123421', False),
                             ('-121', False),
                             ('1-21', False),
                         ])

def test_positive(input_data,expected):
    assert is_palindrome(input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             (1, TypeError),
                             (True, TypeError),
                             ([1], IndexError),
                             ([''], IndexError),
                             ([], IndexError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     is_palindrome(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ('', True),
                             ('1', True),
                             ('12', False),
                             ('  ', True),
                             ('1111', True)
                         ])
def test_bound(input_data,expected):
    assert is_palindrome(input_data) == expected