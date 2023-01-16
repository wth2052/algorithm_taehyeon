#결과는 가장 큰놈 * 그다음 큰놈 return answer
#정렬..은아니고 최댓값뽑기?
def solution(numbers):
    result = sorted(numbers)
    print(result[-1])
    answer = result[-1] * result[-2]
    return answer
