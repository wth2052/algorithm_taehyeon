def solution(s):
    #스택
    #try ~ except (파이썬엔 이런 문법이있구나)
    answer = []
    문자열 = s.split(" ")
    print(문자열)
    #['10', '20', '30', '40']
    for i in 문자열:
        try:
            answer.append(int(i))
        except:
            if 'Z' in 문자열:
                answer.pop()
                print('Z있으니 pop')
    return sum(answer)
    