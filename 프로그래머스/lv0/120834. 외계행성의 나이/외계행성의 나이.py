def solution(age):
    알파벳 = ['a','b','c','d','e','f','g','h','i','j']
    답 = ""
    for i in str(age):
        print(i)
        답 += 알파벳[int(i)]
    return 답