import pytest

import DZ_4.tests.task_1_PersonList_test
from DZ_3.task_10_DList import DList
from main_test import index


@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [1,2]),
                             (3, [1,2,3,None]),
                             (4, [1,2,3,4]),
                             (5, [1,2,3,4,5,None,None])
                         ])

def test_add(input_data,expected):
    dList = DList()
    for i in range(1,input_data+1):
        dList.add(i)
    assert dList.array == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (1, [1]),
                             (2, [2,1]),
                             (3, [3,2,1,None]),
                             (4, [4,3,2,1]),
                             (5, [5,4,3,2,1,None,None])
                         ])

def test_add_front(input_data,expected):
    dList = DList()
    for i in range(1,input_data+1):
        dList.add_front(i)
    assert dList.array == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([],1), -1 ) ,
                             ( ([1],1), 0 ) ,
                             ( ([1,11,1],11), 1 ) ,
                             ( ([''],''), 0 ) ,
                             ( ([1,2,3,1,5,4],5), 4 ) ,
                         ])

def test_find(input_data,expected):
    dList = DList()
    dList.array, item = input_data
    assert dList.find(item) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([1,2,3],0), [2,3]) ,
                             ( ([1,2,3],1), [1,3]) ,
                             ( ([1,2,3],2), [1,2]) ,
                             ( ([1],0), [] )
                         ])

def test_remove_of_index(input_data,expected):
    dList = DList()
    dList.array, index = input_data
    dList.count = len(dList.array)
    dList.remove_of_index(index)
    assert dList.array == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([],1), IndexError) ,
                             ( ([1,2,3],-1), IndexError) ,
                             ( ([1,2,3],3), IndexError)
                         ])

def test_remove_of_index_negative(input_data,expected):
    with pytest.raises(expected):
        dList = DList()
        dList.array, index = input_data
        dList.count = len(dList.array)
        dList.remove_of_index(index)

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([2,4,5,7,8],5), [2,4,7,8]) ,
                             ( ([4],4), []) ,
                             ( ([1,2,3],3), [1,2])
                         ])

def test_remove(input_data,expected):
    dList = DList()
    dList.array, item = input_data
    dList.count = len(dList.array)
    dList.remove(item)
    assert dList.array == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([],1), ValueError) ,
                             ( ([1,2,3],-1), ValueError)
                         ])

def test_remove_negative(input_data,expected):
    with pytest.raises(expected):
        dList = DList()
        dList.array, item = input_data
        dList.count = len(dList.array)
        dList.remove(item)

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([2,4,5,7,5],5), 2) ,
                             ( ([4],4), 1) ,
                             ( ([1,2,3],4), 0)
                         ])

def test_remove(input_data,expected):
    dList = DList()
    dList.array, item = input_data
    dList.count = len(dList.array)
    assert dList.count_item(item) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( ([2,4,5,7,5],66,0), [66,2,4,5,7,5,None,None]) ,
                             ( ([2,4,5,7,5],66,5), [2,4,5,7,5,66,None,None]) ,
                             ( ([2,4,5,7,1],66,5), [2,4,5,7,1,66,None,None]) ,
                             ( ([2,4,5,7,66,None,None],88,4), [2,4,5,7,88,66,None]) ,
                             ( ([2,4,5,7,88,None],0,5), [2,4,5,7,88,0]) ,
                         ])

def test_insert_of_index(input_data,expected):
    dList = DList()
    dList.array, item, index = input_data
    dList.count = 5
    dList.size = len(dList.array)
    dList.insert_of_index(item,index)
    assert dList.array == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             ( [], True) ,
                             ( [1], False)
                         ])

def test_is_empty(input_data,expected):
    dList = DList()
    dList.array = input_data
    dList.size = len(input_data)
    assert dList.is_empty() == expected