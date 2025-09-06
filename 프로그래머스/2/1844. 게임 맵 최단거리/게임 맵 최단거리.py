from collections import deque
def bfs(maps,sy,sx):
    q = deque()
    q.append((sy,sx))
    ly = len(maps)
    lx = len(maps[0])
    if not maps or not maps[0]:
        return -1
    if maps[0][0] == 0:
        return -1
    visited = [[-1] * lx for _ in range(ly)]
    visited[sy][sx] = 1
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    while q:
        y,x = q.popleft()
        if y == ly-1 and x == lx-1:
            return visited[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < ly and 0 <= nx < lx:
                if maps[ny][nx] != 0 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))
    return -1
def solution(maps):
    answer = bfs(maps,0,0)
    return answer
