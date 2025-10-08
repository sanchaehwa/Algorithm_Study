import sys
from collections import deque
input = sys.stdin.readline
N,L,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    ny = [-1,1,0,0]
    nx = [0,0,1,-1]
    total = graph[i][j]
    union = [(i,j)]
    while q:
        y,x = q.popleft()
        for i in range(4):
            sy = ny[i] + y
            sx = nx[i] + x
            if 0 <= sy < N and 0 <= sx < N and not visited[sy][sx]:
                    diff = abs(graph[sy][sx] -graph[y][x])
                    if L <= diff <= R:
                        visited[sy][sx] = True
                        q.append((sy,sx))
                        total += graph[sy][sx]
                        union.append((sy,sx))
    return union,total
days = 0
while True: 
    visited = [[False] * N for _ in range(N)]
    new_graph = [row[:] for row in graph]
    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union,total = bfs(i,j)
                if len(union) > 1:
                    moved = True
                    division = total // len(union)
                    for uy,ux in union:
                        new_graph[uy][ux] = division


    if not moved:
        break
    graph = new_graph
    days += 1
                        
print(days)

                
