def solution(cipher, code):
    암호 = list(cipher)
    #filter로 code간격만큼의 cipher를 return
    count = 0
    정답 = ""
    for i in 암호:
        print(i)
        count += 1 
        if(count % code == 0):
            정답 += i
    return 정답
    # print(list(filter(lambda n : n , 암호)))