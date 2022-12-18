def solution(num_list, n):
    # num_list [1,2,3,4,5,6,7,8]
    # n = i
    print(len(num_list))
    return [num_list[i: i + n] for i in range(0, len(num_list), n)]
    
    