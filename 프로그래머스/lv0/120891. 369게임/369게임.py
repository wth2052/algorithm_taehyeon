def solution(order):

    transform = str(order)
    answer = 0
    answer += transform.count('3')
    answer += transform.count('6')
    answer += transform.count('9')
    print(answer)
    return answer


solution(13579)
