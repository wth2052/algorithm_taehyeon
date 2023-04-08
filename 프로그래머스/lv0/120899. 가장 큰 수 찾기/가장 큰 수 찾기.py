def solution(array):
    #가장 큰수 0
    #인덱스 1
    maxarray = max(array)
    index = array.index(maxarray)
    answer = []
    answer.append(maxarray)
    answer.append(index)
    return answer