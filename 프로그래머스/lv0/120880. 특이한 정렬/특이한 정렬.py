def solution(numlist, n):
    #key=lambda 특정 기준 정렬
    #x numlist 쭉쭉 돌며 절대값을 구함
    #-x인 이유 : -1 / 1이면 큰 값인 1이 앞에와야함
    #-> sort의 두번째 키값으로 -x를 줌
    answer = sorted(numlist, key=lambda x: (abs(x-n), -x))
    return answer