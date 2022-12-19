def solution(quiz):
    answer = []
    for i in quiz:
        a = i.split("=")
        for j in range(len(a)):
            if eval(a[0]) == eval(a[len(a)-1]):
                answer.append("O")
                break
            else:
                answer.append("X")
                break
    return answer
