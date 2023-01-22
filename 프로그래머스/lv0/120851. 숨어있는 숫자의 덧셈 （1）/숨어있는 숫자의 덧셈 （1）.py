import re
    #re를 써서 정규표현식으로 숫자만 걸러 더하기!!!
def solution(my_string):
    result = 0
    numbers = re.sub(r'[^0-9]', '', my_string)

    for i in numbers:
        result += int(i)
    return result