import pytest
from new_DZ_3.DList import DList

@pytest.fixture(scope= 'function')
def dynamic_list():
    return DList()


@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [1,2]),
                             (3, [1,2,3,None]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5,None,None])
                         ])

def test_add(dynamic_list,input_data,expected):
    for i in range(1,input_data+1):
        dynamic_list.add(i)
    assert dynamic_list.get_memory() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [2,1]),
                             (3, [3,2,1,None]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1,None,None])
                         ])

def test_add_front(dynamic_list,input_data,expected):
    for i in range(1,input_data+1):
        dynamic_list.add_front(i)
    assert dynamic_list.get_memory() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([],1), -1 ) ,
                             ( ([1],1), 0 ) ,
                             ( ([1,11,1],11), 1 ) ,
                             ( ([''],''), 0 ) ,
                             ( ([1,2,3,1,5,4],5), 4 )
                         ])

def test_find(dynamic_list,input_data,expected):
    dynamic_list.set_memory(input_data[0])
    assert dynamic_list.find(input_data[1]) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([1,2,3],0), [2,3]) ,
                             ( ([1,2,3],1), [1,3]) ,
                             ( ([1,2,3],2), [1,2]) ,
                             ( ([1],0), [] )
                         ])

def test_remove_of_index(dynamic_list,input_data,expected):
    dynamic_list.set_memory(input_data[0])
    dynamic_list.remove_of_index(input_data[1])
    assert dynamic_list.get_memory() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([],1), IndexError) ,
                             ( ([1,2,3],-1), IndexError) ,
                             ( ([1,2,3],3), IndexError)
                         ])

def test_remove_of_index_negative(dynamic_list,input_data,expected):
    with pytest.raises(expected):
        dynamic_list.set_memory(input_data[0])
        dynamic_list.remove_of_index(input_data[1])

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([2,4,5,7,8],5), [2,4,7,8]) ,
                             ( ([4],4), []) ,
                             ( ([1,2,3],3), [1,2])
                         ])

def test_remove(dynamic_list,input_data,expected):
    dynamic_list.set_memory(input_data[0])
    dynamic_list.remove(input_data[1])
    assert dynamic_list.get_memory() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([],1), ValueError) ,
                             ( ([1,2,3],-1), ValueError)
                         ])

def test_remove_negative(dynamic_list,input_data,expected):
    with pytest.raises(expected):
        dynamic_list.set_memory(input_data[0])
        dynamic_list.remove(input_data[1])

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([2,4,5,7,5],5), 2) ,
                             ( ([4],4), 1) ,
                             ( ([1,2,3],4), 0)
                         ])

def test_count_item(dynamic_list,input_data,expected):
    dynamic_list.set_memory(input_data[0])
    assert dynamic_list.count_item(input_data[1]) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([2,4,5,7,5],66,0), [66,2,4,5,7,5,None,None]) ,
                             ( ([2,4,5,7,5],66,5), [2,4,5,7,5,66,None,None]) ,
                             ( ([2,4,5,7,1],66,5), [2,4,5,7,1,66,None,None]) ,
                             ( ([2,4,5,7,66,None,None],88,4), [2,4,5,7,88,66,None]) ,
                             ( ([2,4,5,7,88,None],0,5), [2,4,5,7,88,0]) ,
                             ( ([2,4,5,7,88,None],0,100), [2,4,5,7,88,0])
                         ])

def test_insert_of_index(dynamic_list,input_data,expected):
    dynamic_list.set_memory(input_data[0])
    dynamic_list.insert_of_index(input_data[1],input_data[2])
    assert dynamic_list.get_memory() == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( [], True) ,
                             ( [1], False)
                         ])

def test_is_empty(dynamic_list,input_data,expected):
    dynamic_list.set_memory(input_data)
    assert dynamic_list.is_empty() == expected