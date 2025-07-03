import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 방향벡터
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

edge_dict = defaultdict(list)  # 섬 번호: 가장자리 리스트

def dfs(i, j, num):
    visited[i][j] = True
    graph[i][j] = num
    for k in range(4):
        nx, ny = j + dx[k], i + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(ny, nx, num)
            elif graph[ny][nx] == 0:
                edge_dict[num].append((i, j))  # 현재 위치(i,j)가 가장자리

def bfs(edge_list, island_num):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for y, x in edge_list:
        q.append((y, x, 0))
        visited[y][x] = 0
    while q:
        y, x, d = q.popleft()
        for dir in range(4):
            ny, nx = y + dy[dir], x + dx[dir]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 0 and visited[ny][nx] == -1:
                    visited[ny][nx] = d + 1
                    q.append((ny, nx, d + 1))
                elif graph[ny][nx] > 1 and graph[ny][nx] != island_num:
                    return d

# 섬 번호 지정 & 가장자리 수집
num = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j, num)
            num += 1

# 가장 짧은 다리 찾기
min_dist = float('inf')
for island_num, edge_list in edge_dict.items():
    dist = bfs(edge_list, island_num)
    if dist is not None:
        min_dist = min(min_dist, dist)

print(min_dist)