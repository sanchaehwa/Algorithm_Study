import random
#numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    #number = [1,2,3,4,5,6,7,8,9]
    number  = list(range(1,10))
    result = []
    for i in number:
        if i not in numbers:
            result.append(i)
    #print(result)
    answer = sum(result)
    return answer
#print(solution(numbers))
