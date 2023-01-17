import math
def solution(array):
    array.sort()
    result = len(array)
    반나눈숫자 = result / 2
    print("나는 어레이",array)
    return(array[math.floor(반나눈숫자)])
