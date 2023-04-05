#재귀를 통해 팩토리얼 구하기
def factorial(number):
    if(number > 1):
        return number*factorial(number-1)
    return number

def solution(n):
    result = 0
    for i in range(1, 11):
        if(n >= factorial(i)):
            result = i
            continue
        else:
            break
    return result