def solution(array, n):
    answer = 0
    for i in array: #배열의 범위만큼 돌고
        for compare_num in array: #배열의 범위만큼 넘버를 비교하며 나갈때
            if compare_num == n: # 비교숫자랑 n매개변수랑 같으면
                answer += 1  #카운트 1올리고
            else:
                continue
        return answer


solution([1, 1, 2, 3, 4, 5], 1)