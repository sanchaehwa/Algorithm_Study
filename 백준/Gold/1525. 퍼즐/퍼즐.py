import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    target = "123456780"
    q = deque()
    q.append((start,0)) #현재 상태 / 이동 횟수
    visited = {start}
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    while q:
        state, cnt = q.popleft()
        if state == target:
            return cnt
        idx = state.index("0")
        y,x = divmod(idx,3) #divmod => 튜플로 반환 / 1차원 -> 2차원
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if  0 <= ny < 3 and 0 <= nx < 3:
                nidx = ny * 3 + nx #2차원 -> 1차원
                new_state = list(state)
                new_state[idx],new_state[nidx] = new_state[nidx],new_state[idx]
                new_state = "".join(new_state)
                if new_state not in visited:
                    visited.add((new_state))
                    q.append((new_state,cnt+1))
    return -1
graph = []
for i in range(3):
    graph.extend(input().split())
start = "".join(graph)
print(bfs(start))