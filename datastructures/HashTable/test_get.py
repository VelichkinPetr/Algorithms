import pytest,random
from HashTable import HashMap

@pytest.mark.parametrize('input_data, expected',
                         [
                             (2, '*2'),
                             (3, '*3'),
                             (4, '*4'),
                             (5, '*5')
                         ])

def test_positive(input_data,expected):
    map = HashMap()
    for i in range(1,input_data+1):
        map.add(i,f'*{i}')
    assert map.get(i) == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (100, [i for i in range(100)]),
                             (1000, [i for i in range(1000)]),
                             (10000, [i for i in range(10000)])
                         ])

def test_bound(input_data,expected):
    map = HashMap()
    text = "hi!"
    texts = []
    rezult = []
    dictionary_abc = "qwertyuiop[]';lkjhgfdsazxcvbnm,./"
    for i in range(input_data):
        index = random.randint(0, len(dictionary_abc) - 1)
        text = text + dictionary_abc[index]
        texts.append(text)
        map.add(text, i)
    for i in texts:
       rezult.append(map.get(i))
    assert rezult == expected

@pytest.mark.parametrize('input_data, expected',
                         [
                             (10, ValueError)
                         ])

def test_negative(input_data,expected):
    with pytest.raises(expected):
        map = HashMap()
        text = "hi!"
        dictionary_abc = "qwertyuiop[]';lkjhgfdsazxcvbnm,./"
        for i in range(input_data):
            index = random.randint(0, len(dictionary_abc) - 1)
            text = text + dictionary_abc[index]
            map.add(text, i)
        map.get(0)

