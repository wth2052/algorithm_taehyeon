def solution(before, after):
    beforeresult = before[::-1]
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0
    