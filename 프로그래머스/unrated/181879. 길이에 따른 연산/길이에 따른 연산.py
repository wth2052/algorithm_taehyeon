def solution(num_list):
    result = 1
    if len(num_list) < 11:
        for i in num_list:
            result *= i
        return result
    return sum(num_list)