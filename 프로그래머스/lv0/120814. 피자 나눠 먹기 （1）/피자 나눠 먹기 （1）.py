def solution(n):
    #7조각씩 잘라줌
    #1~7 1 
    #8~16 2
    #17~21 3 ... 100까지
    #매 7마다 1씩 증가해야함
    result = 0
    for i in range(0, n):
        if i % 7 == 0:
            result += 1
    return result