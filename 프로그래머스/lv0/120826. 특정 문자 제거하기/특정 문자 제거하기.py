import re

def solution(my_string, letter):
    result = re.sub(letter, "", my_string);
    return result