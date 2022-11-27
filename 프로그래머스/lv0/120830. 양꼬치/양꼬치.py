# 양꼬치 n 음료수 k
import math


def solution(n, k):
    yang = 12000
    drink = 2000
    yanggogi = yang * n
    drinks = drink * k
    answer = (yanggogi) + (drinks)
    for i in range(math.trunc(n / 10)): #소숫점 버리기
        if n / 10 > 0:
            answer -= 2000 

    return answer

print(solution(64, 4))