def sum_of_digits(digit):
    if digit < 0:
        raise ValueError
    elif digit == 0:
        return 0
    return digit%10 + sum_of_digits(digit//10)

#print(sum_of_digits(-124))
