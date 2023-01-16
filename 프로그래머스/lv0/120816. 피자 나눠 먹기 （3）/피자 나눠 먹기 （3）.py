#머쓱이 발전했네...

#조각수 slice
#먹는 사람수 n

#
def solution(slice, n):
    result = 0
    for i in range(0, n):
        if i % slice == 0:
            result += 1
    return result