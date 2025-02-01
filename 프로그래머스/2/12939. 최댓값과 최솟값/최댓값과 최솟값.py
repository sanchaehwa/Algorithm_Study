s = "-1 -2 -3 -4"
def solution(s):
    
    list_s = list(map(int,s.split()))
    return f"{min(list_s)} {max(list_s)}"
print(solution(s))