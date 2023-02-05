def solution(numbers, direction):

    result = []
    숫자저장 = 0
    if direction == "right":
        숫자저장 += numbers[-1]
        print(숫자저장)
        numbers.pop()
        numbers.insert(0, 숫자저장)
        return numbers
    elif direction == "left":
        숫자저장 += numbers[0]
        print(숫자저장)
        del numbers[0]
        numbers.append(숫자저장)
    return numbers
    