import pytest,os
from DZ_1.mod_5_task_5 import main

def test_empty_file():
    name_file = 'tests_mod_5_task_5.txt'
    file = open(name_file,'w')
    file.write('')
    with pytest.raises(ValueError):
        main(name_file)

def test_empty_no_one_string():
    name_file = 'tests_mod_5_task_5.txt'
    file = open(name_file,'w')
    file.write('\n')
    with pytest.raises(ValueError):
        main(name_file)

def test_string():
    name_file = 'tests_mod_5_task_5.txt'
    file = open(name_file,'w')
    file.write('aaaa')
    with pytest.raises(ValueError):
        main(name_file)

def test_string_with_enter():
    name_file = 'tests_mod_5_task_5.txt'
    file = open(name_file,'w')
    file.write('aaaa\n')
    with pytest.raises(ValueError):
        main(name_file)

def test_not_found_file():
    name_file = ''
    with pytest.raises(FileNotFoundError):
        main(name_file)

def test_string_and_int():
    output = open('mod_5_task_5_output.txt', 'w')
    output.write('')
    output.close()

    name_file = r'tests_mod_5_task_5.txt'
    file = open(name_file,'w')
    file.write('aaaa\n'
               '23-1-1,4')
    file.close()

    main(name_file)
    assert os.stat('mod_5_task_5_output.txt').st_size != 0

def test_positive():
    output = open('mod_5_task_5_output.txt', 'w')
    output.write('')
    output.close()

    name_file = r'tests_mod_5_task_5.txt'
    file = open(name_file,'w')
    file.write('''date,visitors
2023-01-01,150
2023-01-02,200
2023-01-03,250
2023-01-04,100
2023-01-05,300
2023-01-06,180''')
    file.close()

    main(name_file)
    assert os.stat('mod_5_task_5_output.txt').st_size != 0