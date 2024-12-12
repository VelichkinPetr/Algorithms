def reverse_string(string):
    if string == '' or string == []:
        return ''
    rec = reverse_string(string[1:])
    return rec + string[0]
