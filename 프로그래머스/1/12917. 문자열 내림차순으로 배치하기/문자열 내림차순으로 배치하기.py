#s = "Zbcdefg"
def solution(s):
    answer = "".join(sorted(s, reverse=True))
    print(answer)
    return answer
    
#print(solution(s))