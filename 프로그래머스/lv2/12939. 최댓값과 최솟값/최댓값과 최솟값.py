import numpy as np

def solution(s):
    #배열을 만드는데
    #안에는 string이었던 값들이 각각 i에 담겨 쭉쭉쭉 담김
    #[1, 2, 3, 4]
    정리된배열 = sorted([int(i) for i in s.split()])
    print(정리된배열)
    #문자열 0번째 인덱스를 왼쪽으로
    #문자열 마지막 인덱스를 오른쪽으로 중간에 공백을 하나 둔 값을 리턴
    return str(정리된배열[0]) + ' ' + str(정리된배열[-1])


