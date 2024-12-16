import pytest
from LinkedList import LinkedList

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [2, 1]),
                             (3, [3, 2, 1]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1])
                         ])

def test_add_head(input_data,expected):
    l = LinkedList()
    for i in range(1,input_data+1):
        l.add_head(i)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [1,2]),
                             (3, [1,2,3]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5])
                         ])

def test_add(input_data,expected):
    l = LinkedList()
    for i in range(1,input_data+1):
        l.add(i)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,1), [7,1,2,3,4]),
                             ((7,2), [1,7,2,3,4]),
                             ((7,3), [1,2,7,3,4]),
                             ((7,4), [1,2,3,7,4])
                         ])

def test_insert(input_data,expected):
    l = LinkedList()
    for i in range(1,5):#[1,2,3,4]
        l.add(i)
    l.insert(*input_data)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ((7,0), IndexError),
                             ((7,5), IndexError),
                         ])

def test_insert_negative(input_data,expected):
    with pytest.raises(expected):
        l = LinkedList()
        for i in range(1,5):#[1,2,3,4]
            l.add(i)
        l.insert(*input_data)

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [2,3,4]),
                             (2, [3,4]),
                             (3, [4]),
                             (4, []),
                             (5, [])
                         ])

def test_remove_head(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    for i in range(0,input_data):
        l.remove_head()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1,2,3]),
                             (2, [1,2]),
                             (3, [1]),
                             (4, []),
                             (5, [])
                         ])

def test_remove(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    for i in range(0,input_data):
        l.remove()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [2,3,4]),
                             (2, [1,3,4]),
                             (3, [1,2,4]),
                             (4, [1,2,3])
                         ])

def test_remove_position(input_data,expected):
    l = LinkedList()
    for i in range(1,5): #[1,2,3,4]
        l.add(i)
    l.remove_position(input_data)
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (5, IndexError),
                             (0, IndexError)
                         ])

def test_remove_position(input_data,expected):
    with pytest.raises(expected):
        l = LinkedList()
        for i in range(1, 5):  # [1,2,3,4]
            l.add(i)
        l.remove_position(input_data)

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, []),
                             (1, []),
                             (2, []),
                             (3, []),
                             (4, [])
                         ])

def test_clear(input_data,expected):
    l = LinkedList()
    for i in range(1,input_data):
        l.add(i)
    l.clear()
    assert l.print_LinkedList() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (0, True),
                             (1, False),
                             (2, False),
                             (3, False),
                             (4, False)
                         ])

def test_is_empty(input_data,expected):
    l = LinkedList()
    for i in range(0,input_data):
        l.add(i)

    assert l.is_empty() == expected