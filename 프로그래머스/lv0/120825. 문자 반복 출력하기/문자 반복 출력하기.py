def solution(my_string, n):
    result = ""
    for i in my_string:
        result += i*n
        print(result)
    return result
