#n = 12345
def solution(n):
    return list(map(int, reversed(str(n))))
#print(solution(n))