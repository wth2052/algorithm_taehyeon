def solution(emergency):
    answer = []
    뒤집힌배열 = sorted(emergency, reverse = True)
    
    
    #sort() 리스트 원본값 직접 수정
    #sorted() 정렬 값 반환
    for i in emergency:
        answer.append(뒤집힌배열.index(i)+1)
    return answer