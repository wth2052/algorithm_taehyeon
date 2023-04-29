def solution(s):
    타이틀 = s.title()
    스플릿 = 타이틀.split(" ")
    답안 = []
    for i in 스플릿:
        답안.append(i.capitalize())
    return ' '.join(답안)

