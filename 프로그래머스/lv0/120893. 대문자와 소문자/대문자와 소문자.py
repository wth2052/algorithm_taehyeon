#소문자 아스키코드에서 32를 빼면 해당 대문자 아스키 코드가 나옴
#65~90 대문자
#97~122 소문자
#아스키코드가97보다 작으면 대문자 크면 소문자
#소문자면 32를 빼고
#대문자면 32를 더해라
#아니면 소문자


def solution(my_string):
    result = ""
    num = 1
    for i in my_string:
        if ord(i) >= 97: #97보다 작거나 같으면 더해
            result += chr(ord(i)-32)
            #더해서 바꿔서 돌려주면됨
        else:
            result += chr(ord(i)+32)
    return result
                 

