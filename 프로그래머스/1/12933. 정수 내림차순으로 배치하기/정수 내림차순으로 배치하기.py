#n = 118372
def solution(n):
    str_n = str(n)
    answer = "".join(sorted(str_n,reverse=True))
    return int(answer)
#print(solution(n))