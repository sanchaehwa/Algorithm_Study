from collections import deque
def solution(arr):
    q = deque()
    for n in arr:
        if len(q) == 0 or q[-1] != n: #q[-1] 는 q의 뒤의 원소를 가리킴 그리고 q 가 비어있는 상태일때도 append
            q.append(n)
    return list(q)
print(solution)
    