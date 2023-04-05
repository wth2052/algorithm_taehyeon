#사전순 정렬
def solution(s):
    result = ""
    for i in s:
        # print(s.count(i))
        if s.count(i) == 1:
            result = ''.join(sorted(result + i))
    return result