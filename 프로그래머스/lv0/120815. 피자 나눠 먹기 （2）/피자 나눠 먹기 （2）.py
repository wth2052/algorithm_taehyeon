def solution(n):
    사람수 = n
    피자한판 = 6
    #n이 6 배수 되는 순간까지 계속 증가 시킴
    while 피자한판 % n != 0:
        피자한판=피자한판 + 6
    # 6 배수가 되었다면 나누기 6을 하여 리턴
    return 피자한판 / 6