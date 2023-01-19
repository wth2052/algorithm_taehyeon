import math

def solution(n):
    답 = math.sqrt(n)
    print(답.is_integer())
    if 답.is_integer() == True:
        return 1
    else:
        return 2