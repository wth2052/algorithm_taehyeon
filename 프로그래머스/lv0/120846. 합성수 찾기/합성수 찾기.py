def 합성수인가요(n):
    카운트 = 0
    for i in range(1, n+1):
        if n % i == 0:
            카운트 += 1
    if 카운트 > 2:
        return True
    else:
        return False


def solution(n):
#약수의 개수가 세 개 이상인 수를 합성수
    답안 = 0
    for i in range(1, n+1):
        if 합성수인가요(i):
            답안 += 1
    return 답안
