#n = 121
def solution(n):
    x = 1 
    while x ** 2 <= n:
        if x ** 2 == n:
            answer = (x+1)**2
            return answer
        x += 1
    return -1
#print(solution(n))