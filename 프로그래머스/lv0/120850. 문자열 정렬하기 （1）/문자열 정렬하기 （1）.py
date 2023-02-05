import re

def solution(my_string):
    숫자추출 = re.sub(r'[^0-9]', '', my_string)
    답안 = []
    print(type(숫자추출))
    print(type(답안))
    for i in 숫자추출:
        답안 += i
        찐답안 = map(int, 답안)
    return sorted(찐답안)