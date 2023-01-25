#a e i o u를 제거하기
def solution(my_string):
    모음 = ["a", "e", "i", "o", "u"]
    result = my_string
    for i in 모음:
        for g in my_string:
            if i in result:
                result = result.replace(i, '');
    return result