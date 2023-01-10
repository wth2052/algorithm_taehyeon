def solution(array, height):

    a = array
    b = height
    result = 0
    for i in range(len(a)):
        if (b < a[i]):
            result += 1
    return result