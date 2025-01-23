#n = 10
#result = 3
def solution(n):
    x = 1
    while True:
        if n % x == 1:
            answer = x
            return answer
        x += 1

#print(solution(n))