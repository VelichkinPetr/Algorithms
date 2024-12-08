import random
# Лучший: O(1)
# Средний: O(N)
# Худший: O(N)

#-------------------------------------------------------------------------------
# i < i + 1
# Variant №1
def bubble_sort(array: list[int]) -> list[int]:
    lenght = len(array)

    for i in range(0, lenght, 1):
        for j in range(0, lenght-1-i, 1):
            if array[j] > array[j+1]:

                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

test_array_bubble = [random.randint(-10, 10) for i in range(0, 10, 1)]
print(f"Source array(bubble): {test_array_bubble}")
bubble_sort(test_array_bubble)
print(f"Sorted array(bubble): {test_array_bubble}")
print()
#  end of Variant №1

# Variant №2 + order_by
def bubble_sort(array: list[int], order_by):
    lenght = len(array)

    for i in range(0, lenght, 1):
        for j in range(0, lenght - 1 - i, 1):
            if order_by(array[j], array[j + 1]):
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
test_array_bubble = [random.randint(-10, 10) for i in range(0, 10, 1)]
print(f"Source array(bubble) order_by: {test_array_bubble}")
bubble_sort(test_array_bubble,lambda x,y: x>y)
print(f"Sorted array(bubble) order_by: {test_array_bubble}")
print()
# end of Variant №2 + order by

# Variant №3 + key + order by
class Dog:
    def __init__(self, age):
        self.age = age

def bubble_sort(array, key, order_by= lambda x, y: x < y):
    lenght = len(array)

    for i in range(0, lenght, 1):
        for j in range(0, lenght - 1 - i, 1):
            if order_by( key(array[j]), key(array[j + 1]) ):
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
test_array_bubble_object = [Dog(14), Dog(11), Dog(10), Dog(20), Dog(1)]
bubble_sort(test_array_bubble_object,key=lambda dog:dog.age, order_by=lambda x,y: x>y)
print(f'Sorted array(bubble) object(Dog): {[dog.age for dog in test_array_bubble_object]}')
# end of Variant №3 + key + order by
