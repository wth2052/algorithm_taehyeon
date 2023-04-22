def solution(dots):
    print(dots)
    width = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]
    정답 = width * height
    return 정답
    