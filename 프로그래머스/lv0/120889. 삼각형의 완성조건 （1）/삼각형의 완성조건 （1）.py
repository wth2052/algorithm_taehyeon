def solution(sides):
    
    #가장 큰애가 2,3번째 작은애 더한값보다 작으면
    #1리턴
    #아니면 2리턴
    sides.sort();
    if sides[0]+sides[1] > sides[2]:
        return 1
    else:
        return 2