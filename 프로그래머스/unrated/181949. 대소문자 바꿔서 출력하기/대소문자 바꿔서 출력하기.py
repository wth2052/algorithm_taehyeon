str = input()

def 대소문자(string):
    answer = ""
    for i in str:
        if i.isupper():
            answer += i.lower()
        elif i.islower():
            answer += i.upper()
    print(answer)
    return answer
대소문자(str)
