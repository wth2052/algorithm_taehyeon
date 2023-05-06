# j 루프 범위
# k 포함할 문자열
def solution(i, j, k):
    count = 0
    for number in range(i, j + 1):
        for g in str(number):
            if g in str(k):
                count += 1
    return count
    