def solution(angle):
    if 0 <= angle <= 89: 
        answer = 1
    elif angle == 90:
        answer = 2
    elif 91 <= angle <= 179 :
        answer = 3
    elif angle == 180:
        answer = 4
    return answer