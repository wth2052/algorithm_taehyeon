def solution(array):
    
    counter = 0
    for i in array:
        for h in range(len(str(i))):
            if str(i)[h] == '7':
                counter += 1
    return counter