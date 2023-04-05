#이진수 덧셈
#0 + 0 = 0
#1 + 0 = 1
#0 + 1 = 1
#1 + 1 = 10
#1 + 1 + 1 = 11
#2진수로 변환 bin()
def solution(bin1, bin2):
    b1int = int(bin1, 2)
    b2int = int(bin2, 2)
    result = (bin(b1int + b2int))
    return result.replace('0b','')