def solution(my_string, num1, num2):
    answer = []
    for i in my_string:
        print(i)
        answer.append(i)
    answer[num1], answer[num2] = answer[num2], answer[num1]
    return ''.join(answer)
    