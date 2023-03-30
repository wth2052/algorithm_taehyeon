import math
def solution(num, total):
    # 3 12 
    # 3(-1) 4(3x4=12) 5(+1)
    # 5 15
    # 1(-2) 2(-1) 3(5x3=15) 4(+1) 5(+2)
    # 얘가 배열 가운데값print(total // num)
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)]