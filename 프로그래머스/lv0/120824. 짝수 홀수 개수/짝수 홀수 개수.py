def solution(num_list):
    홀수카운트 = 0
    짝수카운트 = 0
    result = []
    for i in num_list:
        if i % 2 == 0:
            홀수카운트 +=1
        else:
            짝수카운트 +=1
            print(홀수카운트,짝수카운트)
    return [홀수카운트, 짝수카운트]

 