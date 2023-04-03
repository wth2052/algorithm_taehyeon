def solution(my_string):
    my_string = my_string.lower()
    sorted(my_string)
    return ''.join(sorted(my_string))