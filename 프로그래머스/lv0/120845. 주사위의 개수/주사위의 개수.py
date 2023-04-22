def solution(box, n):
    #box 리스트
    #n 주사위 모서리 길이
    #가로 세로 높이
    # 몫 구하기
    print(int(box[0])//n)
    print(int(box[1])//n)
    print(int(box[2])//n)
    넘버1 = int(box[0])//n
    넘버2 = int(box[1])//n
    넘버3 = int(box[2])//n
    answer = 넘버1 * 넘버2 * 넘버3
    return answer
    
    