def indexes_elements_get_target_sum(nums:list[int], target:int) -> list[int]:
    try:
        check_input_type(nums,target)
        check_len_list(nums)
        check_input_range(nums, target)
    except TypeError:
        return []
    except ValueError:
        return []
    rezult = indexes_elements(nums, target)
    return rezult

def check_input_type(nums,tagret):
    if not isinstance(tagret, int):
        raise TypeError('Целеное значение должны быть типа INT')
    elif isinstance(nums,list):
        for num in nums:
            if not isinstance(num,int):
                raise TypeError('Значения в списке должны быть типа INT')
    return True

def check_len_list(nums):
    if len(nums) < 2 or len(nums) > 104:
        raise ValueError('Количество элементов в списке должно быть от 2 до 104')
    return True

def check_input_range(nums,target):
    if target not in range(-109,110):
        raise ValueError('Целеное значение должны быть в диапазоне от -109 до 109')
    for num in nums:
        if num not in range(-109,110):
            raise ValueError('Значения в списке должны быть в диапазоне от -109 до 109')
    return True

def indexes_elements(nums,target):
    index_list = []
    for num in nums:
        if target - num in nums and target - num != num:
            index_list.append(nums.index(num))
            index_list.append(nums.index(target - num))
            return index_list
    return index_list