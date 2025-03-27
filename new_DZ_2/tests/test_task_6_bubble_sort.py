import pytest
from new_DZ_2.task_6_bubble_sort import bubble_sort


class Dog:
    def __init__(self, age):
        self.age = age

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( ([Dog(14), Dog(11), Dog(10), Dog(20), Dog(1)],lambda dog:dog.age, lambda x,y: x>y), [1, 10, 11, 14, 20] ),
                             ( ([Dog(14), Dog(11), Dog(10), Dog(20), Dog(1)],lambda dog:dog.age, lambda x,y: x<y), [20, 14, 11, 10, 1] ),
                             ( ([9, 7, 7, 0, -1, -9, 0, -10, -3, -6],lambda k:k, lambda x,y: x>y), [-10, -9, -6, -3, -1, 0, 0, 7, 7, 9] ),
                             ( ([9, 7, 7, 0, -1, -9, 0, -10, -3, -6],lambda k:k, lambda x,y: x<y), [9, 7, 7, 0, 0, -1, -3, -6, -9, -10] )
                         ])
def test_positive(input_data,expected):
    assert bubble_sort(*input_data) == expected

@pytest.mark.parametrize('input_data,expected',
                         [
                             ( ([9, 7, 7, 0, -1, -9, 0, -10, -3, -6],0, lambda x,y: x>y), TypeError ),
                             ( ([9, 7, 7, 0, -1, -9, 0, -10, -3, -6],lambda k:k, 0), TypeError ),
                             ( ([9, 7, 7, 0, -1, -9, 0, -10, -3, -6],lambda k:k, '0'), TypeError ),
                             ( ([9, 7, 7, 0, -1, -9, 0, -10, -3, -6],'0', lambda x,y: x>y), TypeError ),
                             (([1,2,5,22,8,12,3],-1,3), TypeError),
                             (([1,2,5,22,8,12,3],1,-3), TypeError),
                             (('',lambda k:k, lambda x,y: x<y), TypeError),
                             (([''],lambda k:k, lambda x,y: x<y), TypeError)
                         ])
def test_negative(input_data,expected):
    with pytest.raises(expected):
     bubble_sort(*input_data)

@pytest.mark.parametrize('input_data,expected',
                         [
                             (([],lambda k:k, lambda x,y: x<y), []),
                             (([3,3,3,3,3],lambda k:k, lambda x,y: x<y), [3,3,3,3,3]),
                             (([1,2,3,4,5],lambda k:k, lambda x,y: x<y), [5,4,3,2,1])
                         ])
def test_bound(input_data,expected):
    assert bubble_sort(*input_data) == expected