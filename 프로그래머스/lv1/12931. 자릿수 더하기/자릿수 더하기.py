# 4n + 3 =
# 시간복잡도 = O(n)


def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer