import re
def stringToInt(inputList):
    for i in range(0,len(inputList),):
        inputList[i] = int(inputList[i])
    return inputList

def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    답 = stringToInt(numbers)
    return sum(답)
    