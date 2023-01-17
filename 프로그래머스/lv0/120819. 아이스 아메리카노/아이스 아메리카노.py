#얼죽아...나랑 똑같구나 머쓱아...
#5500마다 [0] 1씩 증가
#5500를 뺐는데 마이너스다?
#그 값을 [1]에 리턴

def solution(money):
    아메리카노1잔 = 5500;
    for i in range(0, 182):
        money = money - 아메리카노1잔
        if money < 0:
            
            return [i, money+5500]
    

    