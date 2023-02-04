def solution(rsp):
#가위(2)일경우 = 주먹(0)을
#바위(0)일경우 = 보(5)를
#보(5)일경우 = 가위(2)으로 바꿔줌
    결과리스트 = list(rsp)
    답 = ""
    for i in 결과리스트:
        if int(i) == 2:
            i = 0
            답 += str(i)
        elif int(i) == 0:
            i = 5
            답 += str(i)
        else:
            i = 2
            답 += str(i)
    return 답

                
        