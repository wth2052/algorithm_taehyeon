from itertools import *
def solution(spell, dic):
    printList = list(permutations(spell, len(spell)))
    answer = []
    for i in printList:
        경우의수들 = ''.join(i)
        answer.append(경우의수들)
    for i in answer:
        if i in dic:
            return 1
        elif i not in dic:
            continue
    return 2

