import sys
from collections import deque
input = sys.stdin.readline

# 방향: 동=1, 서=2, 남=3, 북=4
direction = [(0,1),(0,-1),(1,0),(-1,0)]
# 좌/우 회전 매핑: 현재 방향 -> (왼쪽, 오른쪽)
turn = {
    1: (4,3),  # 동 -> 좌: 북, 우: 남
    2: (3,4),  # 서 -> 좌: 남, 우: 북
    3: (1,2),  # 남 -> 좌: 동, 우: 서
    4: (2,1)   # 북 -> 좌: 서, 우: 동
}

def bfs(sy,sx,sd,ey,ex,ed):
    q = deque()
    q.append((sy-1, sx-1, sd))
    visited = [[[0]*5 for _ in range(N)] for _ in range(M)]
    visited[sy-1][sx-1][sd] = 1

    while q:
        y,x,d = q.popleft()

        # 도착 체크
        if y == ey-1 and x == ex-1 and d == ed:
            print(visited[y][x][d]-1) #0 bassed 이니깐
            return

        # 1~3칸 앞으로 이동
        dy, dx = direction[d-1]
        for i in range(1,4):
            ny = y + dy*i
            nx = x + dx*i
            if not (0 <= ny < M and 0 <= nx < N):
                break
            if graph[ny][nx] == 1:
                break
            if visited[ny][nx][d] == 0:
                visited[ny][nx][d] = visited[y][x][d] + 1
                q.append((ny,nx,d))

        # 좌/우 회전
        for nd in turn[d]:
            if visited[y][x][nd] == 0:
                visited[y][x][nd] = visited[y][x][d] + 1
                q.append((y,x,nd))

# 입력
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
sy,sx,sd = map(int,input().split())
ey,ex,ed = map(int,input().split())

bfs(sy,sx,sd,ey,ex,ed)