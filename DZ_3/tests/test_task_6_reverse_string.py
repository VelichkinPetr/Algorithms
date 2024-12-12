import pytest
from DZ_3.task_6_reverse_string import reverse_string

@pytest.mark.parametrize('input_data, expected', [
    ('12345','54321'),
    ('[3d4f5]',']5f4d3[')
])

def test_positive(input_data,expected):
    assert reverse_string(input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             (1, TypeError),
                             (True, TypeError),
                             ([1], TypeError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     reverse_string(input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             ([], ''),
                             ([''], ''),
                             (['1','2','3','4','5'], '54321'),
                             (['123'],'123')
                         ])
def test_bound(input_data,expected):
    assert reverse_string(input_data) == expected