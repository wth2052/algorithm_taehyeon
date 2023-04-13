from collections import Counter

def solution(array):
    List = []
    #Counter({1: 2, 2: 2})
    counter = Counter(array)
    #[(3, 3), (1, 1), (2, 1), (4, 1)]
    많이출현한순서 = counter.most_common()
    print(많이출현한순서)
    가장큰값 = 많이출현한순서[0][1]
    
    for i in 많이출현한순서:
        if i[1] == 가장큰값:
            List.append(i[0])
    if len(List) >= 2:
        return -1
    else:
        return List[0]