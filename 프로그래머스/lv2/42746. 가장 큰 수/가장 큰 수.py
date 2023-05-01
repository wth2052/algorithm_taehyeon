def solution(numbers):
    if numbers == 0:
        return '0'
    answer = ''
    #itertools?
    #사실 포문을 돌면 안되는게 아닐까?
    #레벨 2의 세계 어렵다.........
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(numbers)))