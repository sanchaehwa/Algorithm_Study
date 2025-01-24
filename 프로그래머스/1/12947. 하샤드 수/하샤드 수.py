x = 13
def solution(x):
    number = list(map(int,str(x)))
   # print(number)
    result = sum(number)
    #print(result)
    while x % result == 0:
        return True
    return False
print(solution(x))