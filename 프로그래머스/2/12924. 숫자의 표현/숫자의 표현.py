n = 15

def solution(n):
    x = [i for i in range(1,n+1)]
    answer = []
    for i in range(len(x)):
        start = i
        end = start
        sum_x = 0
        while end < len(x) and sum_x < n:
            sum_x += x[end]
            end += 1
            if sum_x == n:
                answer.append(x[start:end])
                break
    return len(answer)