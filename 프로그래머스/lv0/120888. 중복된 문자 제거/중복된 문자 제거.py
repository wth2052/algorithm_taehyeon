from collections import OrderedDict
def solution(my_string):
    return ''.join(OrderedDict.fromkeys(my_string))
        
        