def solution(n):
    #나누었을때 나머지가 1이상인것들 > n보다 작은것들
    result = []
    for i in range(1, n+1):
        if i % 2 < 1:
            print('안녕')
        else:
            print(i)
            result.append(i)
            
    return result
    