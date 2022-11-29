import math


def solution(price):
    if 100000 <= price <= 299999:
        answer = price * 0.95
    elif 300000 <= price <= 499999:
        answer = price * 0.90
    elif 499999 < price:
        answer = price * 0.80
    elif 10 <= price <= 99999:
        answer = price
    return math.trunc(answer)
