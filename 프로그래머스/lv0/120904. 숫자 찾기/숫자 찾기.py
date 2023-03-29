def solution(num, k):
    strnum = str(num)
    strnum2 = list(map(int,str(num)))
    result = strnum.find(str(k))
    result2 = int(result) + 1 
    if k in strnum2:
        return result2
    else:
        return result2 -1