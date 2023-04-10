def solution(n):
    #파이썬 map 사용법
    #list(map(int, a))
    #뒤집어야하니 ::-1
    return list(map(int, str(n)))[::-1]