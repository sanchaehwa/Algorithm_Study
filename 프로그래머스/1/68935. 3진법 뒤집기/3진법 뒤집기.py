#n = 125
def solution(n):
    n_str =[]
    answer = 0
    while n != 0:
        n_str.append(n % 3)
        n = n // 3
    n_str.reverse()

    for idx,i in enumerate(n_str):
        
        i = int(i) * (3**idx)
        answer += i
    return answer
#print(solution(n))