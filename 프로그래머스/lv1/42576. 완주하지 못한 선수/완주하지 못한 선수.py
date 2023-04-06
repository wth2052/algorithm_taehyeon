import collections


def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer)[0]