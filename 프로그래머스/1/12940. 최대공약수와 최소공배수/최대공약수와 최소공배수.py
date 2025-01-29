#n = 2
#m = 5
def solution(n,m):
    answer = []
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            answer.append(n*m // i)
            break


    return answer
#print(solution(n,m))